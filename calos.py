

class CalOS:

    # Refers to the current process's PCB
    current_proc = None

    
    def __init__(self):
        self.syscalls = { "test_syscall": self.test_syscall}

    def syscall(self, fname, val0, val1, val2):
        if not fname in self.syscalls:
            print("ERROR: unknown system call", syscall)
            return
        self.syscalls[fname](val0, val1, val2)


    def test_syscall(self, val0, val1, val2):
        print("Test system call called!")


class PCB:
    '''Process control block'''

    STATE = ("READY", "RUNNING", "WAITING")

    next_pid = 1
    
    def __init__(self, name):

        self._name = name
        self._pid = PCB.next_pid
        PCB.next_pid += 1

        self._entry_point = None
        self._mem_low = None
        self._mem_high = None
        self._state = None

        # Used for storing state of the process when it is not running.
        self._registers = {
            'reg0' : 0,
            'reg1' : 0,
            'reg2' : 0,
            'pc': 0
        }

        # If this PCB is in a queue, _next_in_q refers to the next PCB
        # in the queue.  If None, it is not in a queue or is at the end
        # of the queue.
        self._next_in_q = None

    def set_entry_point(self, addr):
        self._entry_point = addr
    def get_entry_point(self):
        return self._entry_point
    def set_memory_limits(self, low, high):
        self._mem_low = low
        self._mem_high = high

    def set_state(self, st):
        self._state = st

    def set_registers(self, registers):
        self._registers = registers

    def __str__(self):
        return "PCB({}): {}, state {}, pc {}".format(self._name, self._pid, self._state,
                                                     self._registers['pc'])
    
