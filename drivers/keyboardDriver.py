from queue import Queue

class KeyboardDriver():

    def __init__(self):
        self._kybd_buffer = Queue(256) # keyboard buffer of 256 "bytes"
        self._debug = False

    def set_debuf(self, debug):
        self._debug = debug

    def read(self) -> str | int:
        if self._kybd_buffer.empty():
            return -1
        return self._kybd_buffer.get(block=False)

    def write(self, char) -> None:
        if self._debug: print("KeyboardController: entered '" + char + "'")
        if self._kybd_buffer.full():
            return -1
        self._kybd_buffer.put(char, block=False)