
class VicOS:
    def __init__(self):
        self.syscalls = { "test_syscall": self.test_syscall}

    def syscall(self, fname, val0, val1, val2):
        if not fname in self.syscalls:
            print("ERROR: unknown system call", syscall)
            return
        self.syscalls[fname](val0, val1, val2)


    def test_syscall(self, val0, val1, val2):
        print("Test system call called!")
