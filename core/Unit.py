from PyQt4 import QtCore

class Unit(QtCore.QObject):
    change_primitive_resource = QtCore.pyqtSignal('QString', int)
    def __init__(self):
        super(Unit, self).__init__()
    
    def on_turn_end(self, turn_number):
        pass
