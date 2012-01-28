from PyQt4 import QtCore

from Unit import *

from NoMoreWorkersError import *

class Producer(Unit):
    
    employee_fired = QtCore.pyqtSignal('QString')
    employee_hired = QtCore.pyqtSignal('QString')
    needs_employee = QtCore.pyqtSignal(Unit, int)
    salary_changed = QtCore.pyqtSignal(float)
    
    def __init__(self):
        super(Producer, self).__init__()
    
    def ready_for_allocation(self):
        pass
