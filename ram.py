RAM_SIZE = 1024


class RAM:
    '''A representation of RAM. You can access it by using indexing operators: [].
    These call __getitem__ and __setitem__ below. Note that this memory holds whatever
    you put into it -- integers, floats, strings, etc. Each is stored in a single location.
    '''
    def __init__(self, size=RAM_SIZE):
        self._minAddr = 0
        self._maxAddr = RAM_SIZE - 1
        self._memory = []   # a list of values.  Could be #s or instructions.
        for i in range(size):
            self._memory.append(0)

    def __getitem__(self, addr):
        '''called when a ram object is indexed/subscripted: ram[3], e.g.'''
        assert self.is_legal_addr(addr)
        return self._memory[addr]

    def __setitem__(self, addr, val):
        '''called when a ram object is indexed/subscripted: ram[3] = 44, e.g.'''
        assert self.is_legal_addr(addr)
        self._memory[addr] = val

    def is_legal_addr(self, addr):
        return self._minAddr <= addr <= self._maxAddr


class MMU:
    """Memory management unit: translate logical addresses to
    physical addresses and check memory limits."""

    def __init__(self, ram):
        self._ram = ram
        self._reloc_register = 0
        self._limit_register = 0

    def set_reloc_register(self, base):
        self._reloc_register = base

    def set_limit_register(self, limit):
        self._limit_register = limit

    def get_val(self, addr):
        self._check_addr(addr)
        return self._ram[addr + self._reloc_register]

    def set_val(self, addr, val):
        self._check_addr(addr)
        self._ram[addr + self._reloc_register] = val

    def _check_addr(self, addr):
        if addr >= self._limit_register:
            # generate trap (software interrupt)
            print("BAD ADDRESS!: too high")

    def get_translated_addr(self, addr):
        """Return the physical address for the given logical address"""
        return addr + self._reloc_register


