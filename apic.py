###################################
# apic.py contains the classes representing the advanced programmable interrupt controllers
# both local apic (LAPIC) and io apic (IOAPIC)
#
# Info on APICs:
# https://en.wikipedia.org/wiki/Advanced_Programmable_Interrupt_Controller
# 
# Author: Kenny Howes - littlekendian.me
#########################
from cpu import CPU
import threading

class LAPIC():
    def __init__(self, cpu: CPU):
        self._cpu = cpu
        self._intr_lock = threading.Lock()
    
    def take_interrupt_mutex(self):
        self._intr_lock.acquire()

    def release_interrupt_mutex(self):
        self._intr_lock.release()

    def set_interrupt(self, intr_val):
        '''Set the interrupt line to be True if an interrupt is raised, or
        False to indicate the interrupt is cleared.
        '''
        assert isinstance(intr_val, bool)
        self._cpu._intr_raised = intr_val

    def add_interrupt_addr(self, addr):
        '''Add the device bus address to the set of devices that have
        raised an interrupt.'''
        self._cpu._intr_addrs.add(addr)
    
class IOAPIC():
    def __init__(self, lapics: list[LAPIC]):
        self._lapics = lapics
        self._intr_lock = threading.Lock()

        self._current_lapic = 0
    
    def take_interrupt_mutex(self):
        self._intr_lock.acquire()

    def release_interrupt_mutex(self):
        self._intr_lock.release()

    def move_to_next_lapic(self):
        # Currently using round robin for giving io interrupts
        self._current_lapic = (self._current_lapic + 1) % len(self._lapics)

    def interrupt(self, addr):
        '''Set the interrupt line to be True if an interrupt is raised, or
        False to indicate the interrupt is cleared,
        and add the device bus address to the set of devices that have
        raised an interrupt.
        '''
        self._lapics[self._current_lapic].set_interrupt(True)
        self._lapics[self._current_lapic].add_interrupt_addr(addr)
        self.move_to_next_lapic()
