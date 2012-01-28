from PyQt4 import QtCore

class Unit(QtCore.QObject):
    
    UNIT = ""
    
    change_primitive_resource = QtCore.pyqtSignal('QString', int)
    to_be_destroyed = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Unit, self).__init__()
    
    def on_turn_end(self, turn_number):
        pass
    
    def display_money(self, amount):
        return "{:.2f}".format(amount)
