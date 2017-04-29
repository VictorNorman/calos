import time
import threading   # for CPU
import vicos


'''
Architecture Description:
There are 3 registers, reg0, reg1, reg2, and a program counter
register, pc.

There are 1024 bytes of RAM, from addresses 0 to 1023.  A word
is two bytes.

Assembly Language Instructions:
mov <src> <dst>   move value from <src> to <dst>
add <val> <dst>   add value to <dst>
sub <val> <dst>   sub value from <dst>

<src> and <dst> can be a register name, a <value>, or *<value>.
*<src> means the contents of RAM at the address <src>.
You cannot move values from one RAM location to another.
<value> can be given in decimal or hexidecimal.
<val> can be a literal value or a register name.

jmp <dst> means change pc to <dst>.
jez <reg> <dst> means change pc to <dst> if register <reg> is 0.
jnz <reg> <dst> means change pc to <dst> if register <reg> is not 0.
jgz <reg> : > 0
jlz <reg> : < 0

end  means end the program

Instructions take up 2 bytes.

Sample program: multiply values in addresses 0 and 2, leaving
result in location 4.

20: mov 0 4	     # put 0 into the destination in case val1 or val2 are 0.
22: mov *0 reg2      # move 1st value to reg2
24: jez reg2 42      # we are done if val1 is 0
26: mov *2 reg1      # move 2nd value to reg1
28: jez reg1 42      # we are done if val2 is 0
30: mov reg2 reg0    # copy reg2 to reg0
32: sub 1 reg1       # loop: subtract 1 from val2
34: jez reg1 40      # if == 0, we are done looping
36: add reg0 reg2    # add reg0 to reg2  where we accumulate result
38: jmp 32           # repeat the loop
40: mov reg2 4       # store result in location 4
42: end

'''

RAM_SIZE = 1024

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
    def __init__(self, num=0):
        threading.Thread.__init__(self)

        self._num = num   # unique ID of this cpu
        # Initialize registers
        self._reg0 = 0
        self._reg1 = 0
        self._reg2 = 0
        self._pc = 0
        self._ram = None
        self._os = None

    def set_pc(self, pc):
        self._pc = pc		# TODO: check this?

    def add_ram(self, ram):
        self._ram = ram

    def add_os(self, os):
        '''register the OS that is managing this CPU.'''
        self._os = os

    def __str__(self):
        res = '''CPU %d: pc %d, reg0 %d, reg1 %d, reg2 %d''' % \
              (self._num, self._pc, self._reg0, self._reg1, self._reg2)
        return res

    def run(self):
        while True:
            print("Executing code at [%d]: %s" % (self._pc, self._ram[self._pc]))
            if not self.parse_instruction(self._ram[self._pc]):
                # False means an error occurred or the program ended, so return
                return
            print(self)
            time.sleep(DELAY_BETWEEN_INSTRUCTIONS)

    def parse_instruction(self, instr):
        '''return False when program is done'''

        # Make sure it is an instruction.  The PC may have wandered into
        # data territory.
        if isinstance(instr, int):
            print("ERROR: Not an instruction: {0}".format(instr))
            return False
            
        instr = instr.replace(",", "")
        words = instr.split()
#         if words[0].endswith(":"):
#            # label  -- TODO: not sure what to do about this now...
#            words = words[1:]   # remove label and continue
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
            self._pc += 2
        elif instr == "mov":
            self.handle_mov(src, dst)
            self._pc += 2
        elif instr == 'add':
            self.handle_add(src, dst)
            self._pc += 2
        elif instr == 'sub':
            self.handle_sub(src, dst)
            self._pc += 2
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
    def handle_jmp(self, dst):
        self._pc = eval(dst)
    def handle_jez(self, src, dst):
        if (src == 'reg0' and self._reg0 == 0) or \
           (src == 'reg1' and self._reg1 == 0) or \
           (src == 'reg2' and self._reg2 == 0) or \
           (src == 'pc' and self._pc == 0):
            self._pc = eval(dst)
        else:
            self._pc += 2
    def handle_jnz(self, src, dst):
        if (src == 'reg0' and self._reg0 != 0) or \
           (src == 'reg1' and self._reg1 != 0) or \
           (src == 'reg2' and self._reg2 != 0) or \
           (src == 'pc' and self._pc != 0):
            self._pc = eval(dst)
        else:
            self._pc += 2
    def handle_jlz(self, src, dst):
        if (src == 'reg0' and self._reg0 < 0) or \
           (src == 'reg1' and self._reg1 < 0) or \
           (src == 'reg2' and self._reg2 < 0) or \
           (src == 'pc' and self._pc < 0):
            self._pc = eval(dst)
        else:
            self._pc += 2
    def handle_jgz(self, src, dst):
        if (src == 'reg0' and self._reg0 > 0) or \
           (src == 'reg1' and self._reg1 > 0) or \
           (src == 'reg2' and self._reg2 > 0) or \
           (src == 'pc' and self._pc > 0):
            self._pc = eval(dst)
        else:
            self._pc += 2

    def _get_value_at(self, addr):
        '''addr is "*<someval>".  return the value from
        RAM at the addr, which might be decimal
        or hex.'''
        addr = eval(addr[1:])
        return self._ram[addr]

    def handle_mov(self, src, dst):
        if dst == 'reg0':
            if src == 'reg0':
                pass   # no op, essentially
            elif src == 'reg1':
                self._reg0 = self._reg1
            elif src == 'reg2':
                self._reg0 = self._reg2
            elif src == 'pc':
                self._reg0 = self._pc
            elif src[0] == '*':
                # TODO: check validity of address.
                self._reg0 = self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg0 = eval(src)   # handles decimal and hex values.
        elif dst == 'reg1':
            if src == 'reg0':
                self._reg1 = self._reg0
            elif src == 'reg1':
                pass
            elif src == 'reg2':
                self._reg1 = self._reg2
            elif src == 'pc':
                self._reg1 = self._pc
            elif src[0] == '*':
                self._reg1 = self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg1 = eval(src)   # handles decimal and hex values.
        elif dst == 'reg2':
            if src == 'reg0':
                self._reg2 = self._reg0
            elif src == 'reg1':
                self._reg2 = self._reg1
            elif src == 'reg2':
                pass
            elif src == 'pc':
                self._reg2 = self._pc
            elif src[0] == '*':
                self._reg2 = self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg2 = eval(src)   # handles decimal and hex values.
        elif dst == 'pc':
            if src == 'reg0':
                self._pc = self._reg0
            elif src == 'reg1':
                self._pc = self._reg1
            elif src == 'reg2':
                self._pc = self._reg2
            elif src == 'pc':
                pass
            elif src[0] == '*':
                self._pc = self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._pc = eval(src)   # handles decimal and hex values.                
        elif dst[0] == '*':
            print("ERROR: cannot assign to a location referred to by a location in RAM")
        else:
            dst = int(eval(dst))
            # Unique operation here: literal value for dst
            # means the address, which we can move a value to.
            if src == 'reg0':
                self._ram[dst] = self._reg0
            elif src == 'reg1':
                self._ram[dst] = self._reg1
            elif src == 'reg2':
                self._ram[dst] = self._reg2
            elif src == 'pc':
                self._ram[dst] = pc
            elif src[0] == '*':
                # Illegal: cannot move from ram to ram
                print("ERROR: cannot move value from RAM to RAM")
            else:
                # Assume it is a literal value
                self._ram[dst] = eval(src)   # handles decimal and hex values.

    def handle_add(self, src, dst):
        if dst == 'reg0':
            if src == 'reg0':
                self._reg0 += self._reg0
            elif src == 'reg1':
                self._reg0 += self._reg1
            elif src == 'reg2':
                self._reg0 += self._reg2
            elif src == 'pc':
                self._reg0 += self._pc
            elif src[0] == '*':
                self._reg0 += self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg0 += eval(src)   # handles decimal and hex values.
        elif dst == 'reg1':
            if src == 'reg0':
                self._reg1 += self._reg0
            elif src == 'reg1':
                self._reg1 += self._reg1
            elif src == 'reg2':
                self._reg1 += self._reg2
            elif src == 'pc':
                self._reg1 += self._pc
            elif src[0] == '*':
                self._reg1 += self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg1 += eval(src)   # handles decimal and hex values.
        elif dst == 'reg2':
            if src == 'reg0':
                self._reg2 += self._reg0
            elif src == 'reg1':
                self._reg2 += self._reg1
            elif src == 'reg2':
                self._reg2 += self._reg2
            elif src == 'pc':
                self._reg2 += self._pc
            elif src[0] == '*':
                self._reg2 += self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg2 += eval(src)   # handles decimal and hex values.
        elif dst == 'pc':
            if src == 'reg0':
                self._pc += self._reg0
            elif src == 'reg1':
                self._pc += self._reg1
            elif src == 'reg2':
                self._pc += self._reg2
            elif src == 'pc':
                self._pc += self._pc
            elif src[0] == '*':
                self._pc += self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._pc += eval(src)   # handles decimal and hex values.                
        elif dst[0] == '*':
            dst = eval(dst[1:])
            if src == 'reg0':
                self._ram[dst] += self._reg0
            elif src == 'reg1':
                self._ram[dst] += self._reg1
            elif src == 'reg2':
                self._ram[dst] += self._reg2
            elif src == 'pc':
                self._ram[dst] += self._pc
            elif src[0] == '*':
                self._ram[dst] += self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._ram[dst] += eval(src)
        elif dst.isdigit():   # TODO: not really good enough.
            print("ERROR: cannot assign to a literal number.")
        else:
            # Assume dst is a number...  not legal
            # TODO: raise an error.
            print("ERROR: Bad instruction.")
        
                 
    def handle_sub(self, src, dst):
        if dst == 'reg0':
            if src == 'reg0':
                self._reg0 -= self._reg0
            elif src == 'reg1':
                self._reg0 -= self._reg1
            elif src == 'reg2':
                self._reg0 -= self._reg2
            elif src == 'pc':
                self._reg0 -= self._pc
            elif src[0] == '*':
                self._reg0 -= self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg0 -= eval(src)   # handles decimal and hex values.
        elif dst == 'reg1':
            if src == 'reg0':
                self._reg1 -= self._reg0
            elif src == 'reg1':
                self._reg1 -= self._reg1
            elif src == 'reg2':
                self._reg1 -= self._reg2
            elif src == 'pc':
                self._reg1 -= self._pc
            elif src[0] == '*':
                self._reg1 -= self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg1 -= eval(src)   # handles decimal and hex values.
        elif dst == 'reg2':
            if src == 'reg0':
                self._reg2 -= self._reg0
            elif src == 'reg1':
                self._reg2 -= self._reg1
            elif src == 'reg2':
                self._reg2 -= self._reg2
            elif src == 'pc':
                self._reg2 -= self._pc
            elif src[0] == '*':
                self._reg2 -= self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._reg2 -= eval(src)   # handles decimal and hex values.
        elif dst == 'pc':
            if src == 'reg0':
                self._pc -= self._reg0
            elif src == 'reg1':
                self._pc -= self._reg1
            elif src == 'reg2':
                self._pc -= self._reg2
            elif src == 'pc':
                self._pc -= self._pc
            elif src[0] == '*':
                self._pc -= self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._pc -= eval(src)   # handles decimal and hex values.                
        elif dst[0] == '*':
            dst = eval(dst[1:])
            if src == 'reg0':
                self._ram[dst] -= self._reg0
            elif src == 'reg1':
                self._ram[dst] -= self._reg1
            elif src == 'reg2':
                self._ram[dst] -= self._reg2
            elif src == 'pc':
                self._ram[dst] -= self._pc
            elif src[0] == '*':
                self._ram[dst] -= self._get_value_at(src)
            else:
                # Assume it is a literal value
                self._ram[dst] -= eval(src)
        else:
            # Assume dst is a number...  not legal
            # TODO: raise an error.
            print("ERROR: cannot assign to a literal number.")

    def handle_call(self, fname):
        self._os.syscall(fname, self._reg0, self._reg1, self._reg2)


class Monitor:
    def __init__(self, ram):
        self._cpu = None		# may have to become a list of cores
        self._debug = False
        self._ram = ram

    def run(self):
        print("Monitor: enter ? to see options.")
        while True:
            try:
                if self._debug:
                    print("State of the CPU is:")
                    print(str(self._cpu) + "\n" + ("-" * 75))

                instr = input("MON> ")
                if instr.strip() == '?':
                    print("C <addr>: put code into RAM starting at addr")
                    print("D <addr>: put data values into RAM starting at addr")
                    print("S <start> <end>: show memory from start to end")
                    print("X <addr>: execute program starting at addr")
                    print("L <addr> <tapename>: load a program from tape to bytes starting at addr")
                    print("W <start> <end> <tapename>: write bytes from start to end to tapen")
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
                if line[-1] == "\n":
                    line = line[:-1]	# remove newline
                if line.isdigit():
                    # data
                    self._ram[addr] = int(line)
                else:
                    # instructions
                    self._ram[addr] = line
                addr += 2
        print("Tape loaded from %d to %d" % (startaddr, addr))

    def _write_program(self, startaddr, endaddr, tapename):
        '''Write memory from startaddr to endaddr to tape (a file).'''
        with open(tapename, "w") as f:
            addr = startaddr
            while addr <= endaddr:
                f.write(str(self._ram[addr]) + "\n")
                addr += 2
        print("Tape written from %d to %d" % (startaddr, addr - 2))

    def _run_program(self, addr):
        self._cpu = CPU()	# creates a new thread
        self._cpu.add_ram(self._ram)
        self._os = vicos.VicOS()
        self._cpu.add_os(self._os)
        self._cpu.set_pc(addr)
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
            curr_addr += 2
            if not self._ram.is_legal_addr(curr_addr):
                print("End of RAM")
                return
        
    def _poke_ram(self, starting_addr):
        curr_addr = int(starting_addr)
        if not self._ram.is_legal_addr(curr_addr):
            print("Illegal address")
            return
        while True:
            data = input("Enter int value ('.' to end) [%d]> " % (curr_addr))
            if data == '.':
                return
            data = int(data)
            # TODO: allow a way to put characters into RAM?
            self._ram[curr_addr] = data
            curr_addr += 2
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
                print("[%04d] %08d" % (curr_addr, val))
            else:
                print("[%04d] %s" % (curr_addr, val))
            curr_addr += 2
        

        
# Main
ram = RAM()
monitor = Monitor(ram) # Like BIOS
monitor.run()

    
