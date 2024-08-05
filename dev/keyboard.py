import threading, time, sys
from queue import Queue
from apic import IOAPIC

class KeyboardController(threading.Thread):
    '''This controller controls a keyboard device that interrupts the
    CPU whenever an input is received.
    '''
    import cpu as cpu
    DELAY = cpu.DELAY_BETWEEN_INSTRUCTIONS

    def __init__(self, io_apic: IOAPIC, dev_id: int, debug=False):
        threading.Thread.__init__(self)
        
        self._io_apic = io_apic # interrupt handler

        # Bus address identifier: used to indicate to the CPU
        # what device has raised an interrupt.
        self._dev_id = dev_id

        self._scancodes = Queue(256) # 256 scancodes for the controller buffer

        self._debug = debug
        if self._debug: print("KeyboardController created!")

    def set_debug(self, debug):
        self._debug = debug
    
    @property
    def io_port(self):
        if self._scancodes.empty():
            raise BufferError("No scancodes in keyboard controller")
        return self._scancodes.get(block=False)

    def run(self):
        if self._debug: print("KeyboardController: running!")
        while True:
            # Interupt when char comes from "keyboard microcontroller"
            if len(sys.stdin) > 0: # TODO: get this working
                self._io_apic.take_interrupt_mutex()
                self._io_apic.interrupt(self._dev_id)
                self._io_apic.release_interrupt_mutex()

            time.sleep(self.DELAY)