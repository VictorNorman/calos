import time
import threading   # for CPU
import vicos
import devices


'''
Architecture Description:
There are 3 registers, reg0, reg1, reg2, and a program counter
register, pc.

There are 1024 words of RAM, from addresses 0 to 1023.  The number
of bits/bytes in a word is not defined:
o Any positive or negative number fits in a word.
o Every instruction, including arguments, fits in a word.
o A string of up to 4 characters fits in a word: this is
  indicated by surrounding the string with single quotes.


Assembly Language Instructions:
mov <src> <dst>   move value from <src> to <dst>
add <val> <dst>   add value to <dst>
sub <val> <dst>   sub value from <dst>

<src> and <dst> can be a register name, a <value>, or *<value>.
*<src> means the contents of RAM at the address <src>.
*<reg> means the contents of RAM at the location referenced by reg.
You cannot move values from one RAM location to another.
<value> can be given in decimal or hexidecimal.
<val> can be a literal value or a register name.

jmp <dst> means change pc to <dst>.
jez <reg> <dst> means change pc to <dst> if register <reg> is 0.
jnz <reg> <dst> means change pc to <dst> if register <reg> is not 0.
jgz <reg> : > 0
jlz <reg> : < 0

end  means end the program

Sample program: multiply values in addresses 0 and 1, leaving
result in location 2.

20: mov 0 4	     # put 0 into the destination in case val1 or val2 are 0.
21: mov *0 reg2      # move 1st value to reg2
22: jez reg2 31      # we are done if val1 is 0
23: mov *1 reg1      # move 2nd value to reg1
24: jez reg1 31      # we are done if val2 is 0
25: mov reg2 reg0    # copy reg2 to reg0
26: sub 1 reg1       # loop: subtract 1 from val2
27: jez reg1 30      # if == 0, we are done looping
28: add reg0 reg2    # add reg0 to reg2  where we accumulate result
29: jmp 26           # repeat the loop
30: mov reg2 2       # store result in location 2
31: end

'''

RAM_SIZE = 1024

MAX_CHARS_PER_ADDR = 4

# Time to delay between executing instructions, in seconds.
DELAY_BETWEEN_INSTRUCTIONS = 0.2

class RAM:
    def __init__(self, size=RAM_SIZE):
        self._minAddr = 0
        self._maxAddr = RAM_SIZE - 1
        self._memory = []   # a list of values.  Could be #s or instructions.
        for i in range(size):
            self._memory.append(0)

    def __getitem__(self, addr):
        return self._memory[addr]

    def __setitem__(self, addr, val):
        self._memory[addr] = val

    def is_legal_addr(self, addr):
        return self._minAddr <= addr <= self._maxAddr


class CPU(threading.Thread):
    def __init__(self, ram, os, startAddr, debug, num=0):
        threading.Thread.__init__(self)

        self._num = num   # unique ID of this cpu
        self._registers = {
            'reg0' : 0,
            'reg1' : 0,
            'reg2' : 0,
            'pc': startAddr
            }

        self._ram = ram
        self._os = os
        self._debug = debug

        # Create Screen and Keyboard controller threads.
        # This is done here so that when the CPU is done running a program,
        # the screen and kbd threads can be killed.  Then if it is told
        # to start up again, it will create new threads (since you cannot
        # restart stopped threads).
        self._screen = devices.ScreenController(self._ram)
        self._kbd = devices.KeyboardController(self._ram)
        self._screen.start()
        self._kbd.start()

    def isregister(self, s):
        return s in ('reg0', 'reg1', 'reg2', 'pc')

    def set_pc(self, pc):
        # TODO: check if value of pc is good?
        self._registers['pc'] = pc

    def __str__(self):
        res = '''CPU {}: pc {}, reg0 {}, reg1 {}, reg2 {}'''.format(
            self._num, self._registers['pc'], self._registers['reg0'],
            self._registers['reg1'], self._registers['reg2'])
        return res

    def run(self):

        while True:
            if self._debug:
                print("Executing code at [%d]: %s" % (self._registers['pc'],
                                                      self._ram[self._registers['pc']]))
            if not self.parse_instruction(self._ram[self._registers['pc']]):
                # False means an error occurred or the program ended, so return
                break
            if self._debug: print(self)
            time.sleep(DELAY_BETWEEN_INSTRUCTIONS)

        self._kbd.stop()
        self._screen.stop()
        self._kbd.join()
        self._screen.join()

    def parse_instruction(self, instr):
        '''return False when program is done'''

        # Make sure it is an instruction.  The PC may have wandered into
        # data territory.
        if isinstance(instr, int):
            print("ERROR: Not an instruction: {}".format(instr))
            return False
            
        instr = instr.replace(",", "")
        words = instr.split()
        instr = words[0]
        if len(words) == 2:
            dst = words[1]    # for jmp and call.
        elif len(words) == 3:
            src = words[1]
            dst = words[2]

        if instr == "call":
            # Call a python function.  Syntax is
            # call fname.  Function fname is a method in 
            # CalOS class and is called with the values in reg0, reg1, and reg2.
            self.handle_call(dst)
            self._registers['pc'] += 1
        elif instr == "mov":
            self.handle_mov(src, dst)
            self._registers['pc'] += 1
        elif instr == 'add':
            self.handle_add(src, dst)
            self._registers['pc'] += 1
        elif instr == 'sub':
            self.handle_sub(src, dst)
            self._registers['pc'] += 1
        elif instr == 'jez':
            self.handle_jez(src, dst)
        elif instr == 'jnz':
            self.handle_jnz(src, dst)
        elif instr == 'jgz':
            self.handle_jgz(src, dst)
        elif instr == 'jlz':
            self.handle_jlz(src, dst)
        elif instr == 'jmp':
            self.handle_jmp(dst)
        elif instr == 'end':
            return False
        return True
        

    # TODO: do error checking in all these.
    # Could check for illegal addresses, etc.
    def handle_jmp(self, dst):
        if self.isregister(dst):
            self._registers['pc'] = self._registers[dst]
        else:
            self._registers['pc'] = eval(dst)
        
    def handle_jez(self, src, dst):
        if not self.isregister(src):
            print("Illegal instruction")
            return
        if self._registers[src] == 0:
            if self.isregister(dst):
                self._registers['pc'] = self._registers[dst]
            else:
                self._registers['pc'] = eval(dst)
        else:
            self._registers['pc'] += 1
            
    def handle_jnz(self, src, dst):
        if not self.isregister(src):
            print("Illegal instruction")
            return
        if self._registers[src] != 0:
            if self.isregister(dst):
                self._registers['pc'] = self._registers[dst]
            else:
                self._registers['pc'] = eval(dst)
        else:
            self._registers['pc'] += 1
            
    def handle_jlz(self, src, dst):
        if not self.isregister(src):
            print("Illegal instruction")
            return
        if self._registers[src] < 0:
            if self.isregister(dst):
                self._registers['pc'] = self._registers[dst]
            else:
                self._registers['pc'] = eval(dst)
        else:
            self._registers['pc'] += 1
            
    def handle_jgz(self, src, dst):
        if not self.isregister(src):
            print("Illegal instruction")
            return
        if self._registers[src] > 0:
            if self.isregister(dst):
                self._registers['pc'] = self._registers[dst]
            else:
                self._registers['pc'] = eval(dst)
        else:
            self._registers['pc'] += 1

    def _get_value_at(self, addr):
        '''addr is "*<someval>".  return the value from
        RAM at the addr, which might be decimal
        or hex.'''
        addr = eval(addr[1:])
        return self._ram[addr]

    def _get_srcval(self, src):
        if self.isregister(src):
            return self._registers[src]
        elif src[0] == '*':
            return self._get_value_at(src)
        else:   # assume src holds a literal value
            return eval(src)    # handles decimal and hex values.
            # TODO: does the above handle putting strings in memory too?  It should
            # allow single characters, perhaps.


    def handle_mov(self, src, dst):
        '''move value from a src to a dst.  src can be one of:
        literal value:          5
        value in memory:        *4
        value in register:      reg2
        dst can be one of:
        memory location:        4
        register name:          reg1
        memory location in reg: *reg1
        You cannot mov a value from RAM into RAM: you must use
        a register.
        '''
        srcval = self._get_srcval(src)

        if self.isregister(dst):
            self._registers[dst] = srcval
        elif dst[0] == '*':    # for *<register>
            if self.isregister(dst[1:]):
                self._ram[self._registers[dst[1:]]] = srcval
            else:
                print("Illegal instruction")
                return
        else:   # assume dst holds a literal value
            self._ram[eval(dst)] = srcval

    def handle_add(self, src, dst):
        srcval = self._get_srcval(src)

        if self.isregister(dst):
            self._registers[dst] += srcval
        elif dst[0] == '*':    # for *<register>
            if self.isregister(dst[1:]):
                self._ram[self._registers[dst[1:]]] += srcval
            else:
                print("Illegal instruction")
                return
        else:   # assume dst holds a literal value
            self._ram[eval(dst)] += srcval

                 
    def handle_sub(self, src, dst):
        srcval = self._get_srcval(src)

        if self.isregister(dst):
            self._registers[dst] -= srcval
        elif dst[0] == '*':    # for *<register>
            if self.isregister(dst[1:]):
                self._ram[self._registers[dst[1:]]] -= srcval
            else:
                print("Illegal instruction")
                return
        else:   # assume dst holds a literal value
            self._ram[eval(dst)] -= srcval

    def handle_call(self, fname):
        self._os.syscall(fname, self._reg0, self._reg1, self._reg2)


class Monitor:
    def __init__(self, ram):
        self._cpu = None		# may have to become a list of cores
        self._debug = False
        self._ram = ram

    def run(self):   # called from monitor._cpu.start()
        print("Monitor: enter ? to see options.")
        while True:
            try:
                if self._debug:
                    print("State of the CPU is:")
                    print(str(self._cpu) + "\n" + ("-" * 75))

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
                    print("! : Toggle debugging on or off -- off at startup.")
                    continue

                # Remove all commas, just in case.
                instr = instr.replace(",", "").upper()

                if instr.startswith("!"):
                    self._debug = not self._debug
                    continue

                try:
                    arg1 = eval(instr.split()[1])
                except:
                    print("Illegal format: ", instr.split()[1])
                    continue
                if instr.startswith('C '):
                    self._enter_program(arg1)
                elif instr.startswith('S '):
                    try:
                        endaddr = eval(instr.split()[2])
                    except:
                        print("Illegal format: ", instr.split()[2])
                        continue
                    self._dump_ram(arg1, endaddr)
                elif instr.startswith('D '):
                    self._poke_ram(arg1)
                elif instr.startswith('X '):
                    self._run_program(arg1)
                elif instr.startswith('L '):
                    try:
                        tapename = instr.split()[2]
                    except:
                        print("Illegal format: ", instr.split()[2])
                        continue
                    self._load_program(arg1, tapename)  # arg1 is startaddr
                elif instr.startswith('W '):
                    try:
                        endaddr = eval(instr.split()[2])
                        tapename = instr.split()[3]
                    except:
                        print("Illegal format: ", instr.split()[2], instr.split()[3])
                        continue
                    self._write_program(arg1, endaddr, tapename)
                else:
                    print("Unknown command")
            except Exception as e:
                print("Bad command or format: ", e.printStackTrace())

    def _load_program(self, startaddr, tapename):
        '''Load a program into memory from a stored tape (a file) starting
        at address startaddr.'''
        with open(tapename, "r") as f:
            addr = startaddr
            for line in f:
                line = line.strip()
                if line == '':
                    continue            # skip empty lines
                if line.startswith('#'):    # skip comment lines
                    continue
                if line.isdigit():
                    # data
                    self._ram[addr] = int(line)
                else:
                    # instructions
                    self._ram[addr] = line
                addr += 1
        print("Tape loaded from %d to %d" % (startaddr, addr))

    def _write_program(self, startaddr, endaddr, tapename):
        '''Write memory from startaddr to endaddr to tape (a file).'''
        with open(tapename, "w") as f:
            addr = startaddr
            while addr <= endaddr:
                f.write(str(self._ram[addr]) + "\n")
                addr += 1
        print("Tape written from %d to %d" % (startaddr, addr - 1))

    def _run_program(self, addr):
        # creates a new thread, passing in ram, the os, and the
        # starting address
        self._cpu = CPU(self._ram, vicos.VicOS(), addr, self._debug)	
        self._cpu.start()		# call run()
        self._cpu.join()		# wait for it to end


    def _enter_program(self, starting_addr):
        # TODO: must make sure we enter program starting on even boundary.
        curr_addr = int(starting_addr)
        if not self._ram.is_legal_addr(curr_addr):
            print("Illegal address")
            return
        while True:
            code = input("Enter code ('.' to end) [%d]> " % (curr_addr))
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
            data = input("Enter value (. to end) [%d]> " % (curr_addr))
            if data == '.':
                return
            if data[0] == "'":    # user entering string, max 4 characters.
                end = data.find("'", 1)
                if end == -1:
                    print("Bad string: no ending quote")
                    return
                if end > 5:
                    end = 5   # max 4 characters
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
ram = RAM()

# Like BIOS
monitor = Monitor(ram) 
monitor.run()


    
