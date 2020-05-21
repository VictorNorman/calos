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
