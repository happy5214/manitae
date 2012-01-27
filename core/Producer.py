from PyQt4 import QtCore

from Unit import *

from NoMoreWorkersError import *

class Producer(Unit):
    
    needs_employee = QtCore.pyqtSignal(Unit, int)
    
    def __init__(self):
        super(Producer, self).__init__()
    
    def ready_for_allocation(self):
        pass
