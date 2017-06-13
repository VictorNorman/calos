__author__ = 'vtn2'

class Keyboard:
    '''This device uses 2 locations: 0x0 (DATA) and 0x1 (CTRL).
    The device produces characters only when CTRL = 0.  At that
    point the device produces the character into DATA and sets
    CTRL to 1.

    The OS only reads a character when CTRL = 1, and when it is
    finished reading, it sets CTRL to 0.
    '''

    pass

