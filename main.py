##########################
# main.py handles all the set up for CalOS -
# everything needed get the OS to a running state
# bios/uefi, bootloader, and hardware initialization
# that would happen through those.
# Then it runs the OS and allows user interaction
#
# Run with 'python3 main.py'
######################
import calos
from cpu import CPU, MAX_CHARS_PER_ADDR
from apic import LAPIC, IOAPIC
from ram import RAM
from dev.keyboard import KeyboardController
from dev.timer import TimerController

###### Settings
NUMBER_OF_CORES = 2
RAM_SIZE = 1024

# Interrrupt device ids
SOFTWARE_TRAP_DEV_ID = 0
TIMER_DEV_ID  = 1
KYBD_DEV_ID   = 2
SCREEN_DEV_ID = 3
###### End Settings

class Monitor:
    def __init__(self, ram):
        self._debug = False
        self._ram = ram

        self._os = calos.CalOS(ram)
        
        # set up cores with local interrupt controllers
        self._cpus = [CPU(self._ram, self._os, cpu_id) for cpu_id in range(NUMBER_OF_CORES)]
        self._lapics = [LAPIC(self._cpus[i]) for i in range(NUMBER_OF_CORES)]
        self._os.set_cpus(self._cpus)

        # set up the IO interrupt controller
        self._io_apic = IOAPIC(self._lapics)

        # set up peripherals
        self._timer = TimerController(self._io_apic, TIMER_DEV_ID, self._debug)
        self._kybd = KeyboardController(self._io_apic, KYBD_DEV_ID, self._debug)
        self._os.set_data_ports([self._timer, self._kybd])

        self.set_debug(False)

    def run(self):
        print("Monitor: enter ? to see options.")
        while True:
            if self._debug:
                for cpu in self._cpus:
                    print(cpu)
                print("-" * 75)

            instr = input("MON> ").strip()
            if instr == '':
                # blank line
                continue
            if instr == '?':
                print("C <addr>: put code into RAM starting at addr")
                print("D <addr>: put data values into RAM starting at addr")
                print("S <start> <end>: show memory from start to end")
                print("X <addr>: execute program starting at addr")
                print("L <addr> <tapename>: load a program from tape to bytes starting at addr")
                print("W <start> <end> <tapename>: write bytes from start to end to tape")
                print("R : Start up OS and execute ready queue")
                print("Q : Leave the OS")
                print("! : Toggle debugging on or off -- off at startup.")
                continue

            # Remove all commas, just in case
            instr = instr.replace(",", "")
            
            # 0 argument cases
            numargs = len(instr.split())
            if numargs == 1:
                self._zero_arg_instr(instr)
            elif numargs == 2:
                self._one_arg_instr(instr)
            elif numargs == 3:
                self._two_arg_instr(instr)
            elif numargs == 4:
                self._three_arg_instr(instr)
            else:
                print("Unknown or badly formatted instruction: too many arguments")

    def _zero_arg_instr(self, instr):
        # Uppercase to not worry about user input being in any case
        instr = instr.upper()
        if instr.startswith("!"):
            self.set_debug(not self._debug)
        elif instr.startswith("R"):
            self._os.run()
        elif instr.startswith("Q"):
            # TODO: make this involve giving up the lock from the CPU
            exit()
        else:
            print("Unknown command")

    def _one_arg_instr(self, instr):
        instr = instr.upper()
        try:
            arg1 = eval(instr.split()[1])
        except:
            print("Illegal format: ", instr.split()[1])
            return
        if instr.startswith('C '):
            self._enter_program(arg1)
        elif instr.startswith('D '):
            self._poke_ram(arg1)
        elif instr.startswith('X '):
            self._run_program(arg1)
        else:
            print("Unknown command")

    def _two_arg_instr(self, instr):
        # upper()'s done in the condition only to preserve tapename for Load
        if instr.upper().startswith('S '):
            try:
                startaddr = eval(instr.split()[1])
                endaddr = eval(instr.split()[2])
                self._dump_ram(startaddr, endaddr)
            except:
                print("Illegal format")

        elif instr.upper().startswith('L '):
            try:
                startaddr = eval(instr.split()[1])
                tapename = instr.split()[2]
                self._load_program(startaddr, tapename)
            except:
                print("Illegal format")
        else:
            print("Unknown command")


    def _three_arg_instr(self, instr):
        if instr.upper().startswith('W '):
            try:
                startaddr = eval(instr.split()[1])
                endaddr = eval(instr.split()[2])
                tapename = instr.split()[3]
                self._write_program(startaddr, endaddr, tapename)
            except:
                print("Illegal format")
        else:
            print("Unknown command")

    def set_debug(self, debug):
        self._debug = debug
        for cpu in self._cpus:
            cpu.set_debug(self._debug)
        self._os.set_debug(self._debug)

    def _load_program(self, startaddr, tapename, procname=None):
        '''Load a program into memory from a stored tape (a file) starting
        at address startaddr.  Create a PCB for the program and add to
        the ready q.  Use the first part of the tapename as the procname,
        if not provided. 
        '''
        
        if procname is None:
            # Lop off .* from the end.
            procname = tapename[: tapename.find(".")]
        pcb = None
        try:
            with open(tapename, "r") as f:
                pcb = calos.PCB(procname)
                if self._debug:
                    print("Created PCB for process {}".format(procname))
                addr = startaddr
                pcb.set_low_mem(addr)
                for line in f:
                    line = line.strip()
                    if line == '':
                        continue            # skip empty lines
                    if line.startswith('#'):    
                        continue	    # skip comment lines
                    if line.isdigit():      # data
                        self._ram[addr] = int(line)
                        addr += 1
                    elif line.startswith("__main:"):
                        self._handle_main_label(addr, line, pcb)
                    elif line.startswith("__data:"):
                        self._handle_data_label(addr, line, pcb)
                    elif line.startswith("db "): # define all the specified bytes in ram

                        # figure out what to define
                        bytes = eval(line.split()[1])
                        self._handle_db(addr, bytes)

                        # move address head forward the respective number of bytes
                        if type(bytes) == str:
                            addr += len(bytes)
                        else: addr += 1

                    else:   # the line is regular code: store it in ram
                        self._ram[addr] = line
                        addr += 1
            print("Tape loaded from {} to {}".format(startaddr, addr - 1))
            if self._debug:
                print(pcb)
        except FileNotFoundError:
            print("File not found")
        if pcb is not None:
            self._os.add_to_ready_q(pcb)

    def _handle_main_label(self, addr, line, pcb):
        """line from the file has format __main: <addr>,
        which indicates where the entry point is.  Note: all
        addresses in the code are logical.
        e.g., __main: 0 means the code assumes
        the executable lives at 0.  It might be loaded
        into some other location, which is the value in addr.
        """
        if len(line.split()) != 2:
            raise ValueError("Illegal format: __main: must be followed by entrypoint address.")
        logical_addr = int(line.split()[1])
        pcb.set_entry_point(logical_addr)
        if self._debug:
            print("__main found at physical location", addr, "but logical addr", logical_addr)

    def _handle_data_label(self, addr, line, pcb):
        """line from the file has format __data: <size>,
        which indicates how many bytes are needed to store data for the program.
        NOTE NOTE NOTE: we assume this label, if found, is immediately after the
        code.
        """
        if len(line.split()) != 2:
            raise ValueError("Illegal format: __data: must be followed by # of bytes.")
        num_bytes = int(line.split()[1])
        pcb.set_high_mem(addr + num_bytes)
        if self._debug:
            print("__data found at physical location", addr, "with size", num_bytes)
            print("high memory limit set at", addr + num_bytes)

    def _handle_db(self, addr, bytes):
        offset = 0
        for byte in bytes:
            self._ram[addr + offset] = byte
            offset += 1

    def _write_program(self, startaddr, endaddr, tapename):
        '''Write memory from startaddr to endaddr to tape (a file).'''
        with open(tapename, "w") as f:
            addr = startaddr
            while addr <= endaddr:
                f.write(str(self._ram[addr]) + "\n")
                addr += 1
        print("Tape written from {} to {}".format(startaddr, addr - 1))

    def _run_program(self, addr):
        # Set the program counter and start the CPU running.
        self._cpus[0].set_pc(addr)
        self._cpus[0].start()		# call run()
        self._cpus[0].join()		# wait for it to end

    def _enter_program(self, starting_addr):
        # TODO: must make sure we enter program starting on even boundary.
        curr_addr = int(starting_addr)
        if not self._ram.is_legal_addr(curr_addr):
            print("Illegal address")
            return
        while True:
            code = input("Enter code ('.' to end) [{}]> ".format(curr_addr))
            if code == '.':
                return
            self._ram[curr_addr] = code
            curr_addr += 1
            if not self._ram.is_legal_addr(curr_addr):
                print("End of RAM")
                return
        
    def _poke_ram(self, starting_addr):
        curr_addr = int(starting_addr)
        if not self._ram.is_legal_addr(curr_addr):
            print("Illegal address")
            return
        while True:
            data = input("Enter value (. to end) [{}]> ".format(curr_addr))
            if data == '.':
                return
            if data[0] == "'":    # user entering string, max 4 characters.
                end = data.find("'", 1)
                if end == -1:
                    print("Bad string: no ending quote")
                    return
                if end > MAX_CHARS_PER_ADDR:
                    end = MAX_CHARS_PER_ADDR
                data = data[0:end] + "'"
                self._ram[curr_addr] = data
            else:
                try:
                    data = int(data)
                except:
                    print("Bad value")
                    return
                self._ram[curr_addr] = data
            curr_addr += 1
            if not self._ram.is_legal_addr(curr_addr):
                print("End of RAM")
                return

    def _dump_ram(self, starting_addr, ending_addr):
        curr_addr = int(starting_addr)
        if not self._ram.is_legal_addr(curr_addr):
            print("Illegal start address")
            return
        end_addr = int(ending_addr)
        if not self._ram.is_legal_addr(end_addr):
            print("Illegal end address")
            return
        if end_addr < curr_addr:
            print("Nothing to display")
            return
        while curr_addr <= end_addr:
            val = self._ram[curr_addr]
            if isinstance(val, int):
                print("[%04d] %d" % (curr_addr, val))
            else:
                print("[%04d] %s" % (curr_addr, val))
            curr_addr += 1
        
# Main
ram = RAM(RAM_SIZE)

# Like BIOS
monitor = Monitor(ram)
monitor.run()
