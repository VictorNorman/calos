'''Devices that interact with the CPU: I/O ports, timer, etc.'''

import threading
import time
import cpu

class TimerController(threading.Thread):
    '''This controller controls a timer device that interrupts the
    CPU whenever the timer runs down to 0.
    '''

    DELAY = cpu.DELAY_BETWEEN_INSTRUCTIONS

    def __init__(self, cpu, dev_id):
        threading.Thread.__init__(self)
        self._cpu = cpu

        # Bus address identifier: used to indicate to the CPU
        # what device has raised an interrupt.
        self._dev_id = dev_id
        self._countdown = 0
        self._mutex = threading.Lock()
        print("TimerController created!")

    def set_countdown(self, val):
        '''Set the number of seconds until the timer fires.
        '''
        with self._mutex:
            self._countdown = val
        print("Timer: set countdown to", self._countdown)

    def run(self):
        '''When running, count down from _countdown to 0, and then
        raise an interrupt.  When not running, periodically see if
        the countdown value has been set -- enabling the timer again.
        '''

        print("TimerController: running!")
        while True:
            # Copy value to local variable
            with self._mutex:
                countdown = self._countdown
                
            if countdown > 0:
                countdown -= 1
            if countdown == 0:
                # timer expired!
                self._cpu.take_interrupt_mutex()
                self._cpu.add_interrupt_addr(self._dev_id)
                self._cpu.set_interrupt(True)
                self._cpu.release_interrupt_mutex()
                # Don't generate another interrupt until the
                # previous one is handled and the interrupt is
                # reset.
                countdown = -1
            else: # countdown < 0: indicating do nothing.
                pass

            with self._mutex:
                self._countdown = countdown

            time.sleep(self.DELAY)


class KeyboardController(threading.Thread):
    '''This device receives input from a keyboard.

    Its controller uses 3 addresses to communicate with the CPU:
    o 997: status
      o bit 0: busy
    o 998: control
      o bit 0 = command-ready
      o bit 2 = read
    o 999: data-in

    The KeyboardController waits for the command-ready bit and read bits to be set.
    When they are, it sets the busy bit to 1.  Then it writes keyboard
    characters to the data-in location -- a string up of to 4 characters,
    starting and ending with single quotes. 
    Then, it clears the command-ready and busy bits.
    '''
    STATUS_REG = 997
    CTRL_REG = 998
    DATA_IN_REG = 999
    DELAY = 1    # much slower than the CPU

    def __init__(self, ram, cpu, dev_id):
        threading.Thread.__init__(self)
        self._chars_buf = []
        self._ram = ram
        self._cpu = cpu
        self._stopped = False
        # Bus address identifier: used to indicate to the CPU
        # what device has raised an interrupt.
        self._dev_id = dev_id

    def stop(self):
        self._stopped = True

    def run(self):
        # Following code reads from keyboard without waiting for newline to be entered.
        # https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
        import tty, sys, termios
        fd = sys.stdin.fileno()
        oldSettings = termios.tcgetattr(fd)
        tty.setcbreak(fd)    # get one character, as soon as it is typed.
        while not self._stopped:
            # Always be reading characters from the keyboard, storing the
            # last 4 characters.
            charFromKb = sys.stdin.read(1)
            # print("KeyboardController: Got character -->{}<--".format(charFromKb))
            # keep list to 4 characters at most
            if len(self._chars_buf) == 4:
                # remove the oldest key from the list.
                self._chars_buf.pop(0)
            self._chars_buf.append(charFromKb)

            if self._ram[self.CTRL_REG] & 0x1 == 0x1:
                # command-ready bit is set.
                if self._ram[self.CTRL_REG] & 0x4 == 0x4:
                    # 0x4 means read bit is set
                    self._ram[self.STATUS_REG] = 1   # set the busy bit
                    # buffered characters list might be empty:  OK?
                    data = "'" + "".join(self._chars_buf) + "'"
                    self._ram[self.DATA_IN_REG] = data
                    # clear command-ready and read bits, and busy bits.
                    self._ram[self.CTRL_REG] = 0
                    self._ram[self.STATUS_REG] = 0
                    self._cpu.add_interrupt_addr(self._dev_id)
                    self._cpu.set_interrupt(True)
            time.sleep(self.DELAY)
        # reset tty to old settings.
        termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)
        # print("KBD thread: done!")
        

class ScreenController(threading.Thread):
    '''This device shows output on a screen.

    Its controller uses 3 addresses to communicate with the CPU:
    o 1020: status
      o bit 0: busy
    o 1021: control
      o bit 0 = command-ready
      o bit 1 = write
    o 1022: data-out

    The ScreenController waits for the command-ready bit and write bits to be set.  When they
    are, it sets the busy bit to 1.  Then it reads the data-out location, which will contain
    a string up of to 4 characters, starting and ending with single quotes.  It writes these
    characters out to the screen, and clears the command-ready and busy bits.
    '''

    STATUS_REG = 1020
    CTRL_REG =   1021
    DATA_OUT_REG = 1022
    DELAY = 0.5     # 1/2 second: much slower than CPU

    def __init__(self, ram, cpu, dev_id):
        threading.Thread.__init__(self)
        self._ram = ram
        self._stopped = False
        # Indicates it bus address identifier: used to indicate to the CPU
        # what device # has raised an interrupt.
        self._dev_id = dev_id

    def stop(self):
        self._stopped = True

    def run(self):
        while not self._stopped:
            if self._ram[self.CTRL_REG] & 0x1 == 0x1:
                # command-ready bit is set.
                self._ram[self.STATUS_REG] = 1   # set the busy bit
                if self._ram[self.CTRL_REG] & 0x2 == 0x2:
                    # write bit is set
                    data = self._ram[self.DATA_OUT_REG]
                    # print("SCREEN> " + str(eval(data)))
                    # clear command-ready and write, data-out, and busy bits.
                    self._ram[self.CTRL_REG] = 0
                    self._ram[self.DATA_OUT_REG] = 0
                    self._ram[self.STATUS_REG] = 0
            # else:
                # print("SCREEN> nothing to print")
            time.sleep(self.DELAY)

            
