from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSignal, pyqtProperty, pyqtSlot

class Unit(QtCore.QObject):
    
    UNIT = ""
    id_inc = 1
    level = -1
    
    change_primitive_resource = pyqtSignal('QString', int)
    name_changed_sig = pyqtSignal()
    to_be_destroyed = pyqtSignal()
    
    def __init__(self):
        super(Unit, self).__init__()
        self.id = Unit.id_inc
        Unit.id_inc += 1
        self._name = ''
    
    def __str__(self):
        if not(self.name):
            return "{0} (Level {1}): id {2}".format(self.UNIT, self.level, str(self.id))
        else:
            return self.name
    
    def on_turn_end(self, turn_number):
        pass
    
    def display_money(self, amount):
        return "{:.2f}".format(amount)
    
    @pyqtProperty(str)
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        self.name_changed_sig.emit()
