import devices


DEFAULT_QUANTUM = 3   # very short -- for pedagogical reasons.

class CalOS:

    # Refers to the current process's PCB
    # None means that the "idle process" is current.
    current_proc = None

    
    def __init__(self, ram):
        self.syscalls = { "test_syscall": self.test_syscall}
        self._ready_q = []
        self._ram = ram
        self._timer_controller = None
        self._cpu = None

        # Create the IDLE process, with pid 0
        self._idle_proc = PCB("IDLE", 0)
        self.add_to_ready_q(self._idle_proc)
        # Hard-code into RAM the IDLE process's code.  It simply jmps to its own
        # location forever.
        self._ram[0] = "jmp 0"
        self._idle_proc.set_entry_point(0)
        self._idle_proc.set_quantum(1)
        self._idle_proc.set_memory_limits(0, 0)

        # Stop the OS when there are no more active processes -- processes that
        # have not hit their "end" statement.
        self._active_processes = 0

    def set_cpu(self, cpu):
        self._cpu = cpu

    def syscall(self, fname, val0, val1, val2):
        if not fname in self.syscalls:
            print("ERROR: unknown system call", syscall)
            return
        self.syscalls[fname](val0, val1, val2)

    def test_syscall(self, val0, val1, val2):
        print("Test system call called!")

    def set_timer_controller(self, t):
        self._timer_controller = t

    def add_to_ready_q(self, pcb):
        '''Add to the ready queue, and set the state of the process to READY.
        Make sure the IDLE process is always last in the queue -- so insert before
        it.'''
        if pcb.get_pid() == 0:
            # IDLE process being added to the queue -- put it at the end.
            self._ready_q.append(pcb)
        else:
            if len(self._ready_q) == 0:
                # Nothing in the ready queue, so we'll just stick this process
                # at the end.  The current process must be the idle process.
                assert CalOS.current_proc.get_pid() == 0
                self._ready_q.append(pcb)
            else:
                # assert last item in queue is the IDLE process pcb.
                assert self._ready_q[-1].get_pid() == 0
                # Add pcb to 2nd-to-last slot, leaving IDLE process last.
                self._ready_q.insert(-1, pcb)
        pcb.set_state(PCB.READY)

        print("add_to_ready_q: queue is now:")
        for p in self._ready_q:
            print(p)

    def timer_isr(self):
        '''Called when the timer expires. If there is no process in the
        ready queue or the only process is the IDLE process, reset the timer
        and continue.  Else, context_switch.
        '''

        if self._debug:
            print("End of quantum!")
        # if no other processes ready or one process is ready and it is the 
        # idle process (which should always be ready, actually).
        if len(self._ready_q) == 0 or \
           (len(self._ready_q) == 1 and self._ready_q[0].get_pid() == 0):
            # Leave current proc in place, as running: just reset the timer.
            self.reset_timer()
            return

        old_proc = CalOS.current_proc
        new_proc = self._ready_q.pop(0)
        assert new_proc.get_state() == PCB.READY
        print("Switching procs from {} to {}".format(old_proc.get_name(), new_proc.get_name()))

        self.context_switch(new_proc)

        old_proc.set_state(PCB.READY)
        self.add_to_ready_q(old_proc)
        new_proc.set_state(PCB.RUNNING)
        CalOS.current_proc = new_proc

        # reset the timer (to the quantum of the (new) current_proc).
        self.reset_timer()
    

    def context_switch(self, new_proc):
        '''Do a context switch between the current_proc and the given new_proc, by
        just saving the registers of the current_proc in its PCB and loading the registers
        of the new_proc from its PCB.
        NOTE: does not support recursion!
        NOTE: does not change the state of either proc.
        NOTE: does not change current_proc
        '''

        old = CalOS.current_proc
        old.set_registers(self._cpu.get_registers())
        self._cpu.set_registers(new_proc.get_registers())

    def reset_timer(self):
        '''Reset the timer's countdown to the value in the current_proc's
        PCB.'''
        self._timer_controller.set_countdown(CalOS.current_proc.get_quantum())
        

    def run(self, cpu):
        '''Startup the timer controller and execute processes in the ready
        queue on the given cpu -- i.e., run the operating system!
        '''

        self._active_processes = len(self._ready_q) - 1 # don't count IDLE proc

        # To get things going, have to set the timer to the quantum of
        # the soon-to-be first process, before starting the controller.
        CalOS.current_proc = self._ready_q[0]
        self.reset_timer()
        self._timer_controller.start()

        while self._active_processes > 0:
            CalOS.current_proc = self._ready_q.pop(0)
            CalOS.current_proc.set_state(PCB.RUNNING)
            self.reset_timer()
            self._cpu.set_registers(CalOS.current_proc.get_registers())

            print("Running", CalOS.current_proc)

            cpu.run_process()

            CalOS.current_proc.set_state(PCB.DONE)
            print("Done running", CalOS.current_proc)
            self._active_processes -= 1


class PCB:
    '''Process control block'''

    NEW, READY, RUNNING, WAITING, DONE = "NEW", "READY", "RUNNING", "WAITING", "DONE"
    LEGAL_STATES = NEW, READY, RUNNING, WAITING, DONE

    # PID 0 is reserved for the IDLE process, which runs when there are no other
    # ready processes.
    next_pid = 1
    
    def __init__(self, name, pid=None):

        self._name = name
        if pid is None:
            self._pid = PCB.next_pid
            PCB.next_pid += 1
        else:
            self._pid = pid

        self._entry_point = None
        self._mem_low = None
        self._mem_high = None
        self._state = PCB.NEW

        # Used for storing state of the process's registers when it is not running.
        self._registers = {
            'reg0' : 0,
            'reg1' : 0,
            'reg2' : 0,
            'pc': 0
            }

        # Quantum: how long this process runs before being interrupted.
        self._quantum = DEFAULT_QUANTUM

    def set_entry_point(self, addr):
        self._entry_point = addr
        self._registers['pc'] = addr

    def get_entry_point(self):
        return self._entry_point

    def set_memory_limits(self, low, high):
        self._mem_low = low
        self._mem_high = high

    def set_state(self, st):
        assert st in self.LEGAL_STATES
        self._state = st

    def get_state(self):
        return self._state

    def set_registers(self, registers):
        '''make a copy of the dictionary being passed in, so that we
        don't have multiple references to it.'''
        self._registers = dict(registers)
                
    def get_registers(self):
        return self._registers

    def get_quantum(self):
        return self._quantum
    def set_quantum(self, q):
        self._quantum = q

    def get_pid(self):
        return self._pid

    def get_name(self):
        return self._name

    def __str__(self):
        return "PCB({}): {}, state {}, entrypoint {}".format(self._pid, self._name, self._state,
                                                             self._entry_point)
    
