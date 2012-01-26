from PyQt4.QtCore import pyqtSignal, pyqtProperty, pyqtSlot
from PyQt4.QtGui import QWidget

from core.Producer import Producer
from ui_Hunter import Ui_Hunter

class Hunter(Producer):
    
    def __init__(self):
        super(Hunter, self).__init__()
        self._production_rate = 3
        self._employees = 1
        self._production_on = True
        self.ui = Ui_Hunter()
        self.widget = QWidget()
        self.ui.setupUi(self.widget)
        
        self.ui.prodOnCheckBox.toggled.connect(self.production_on_checked)
        self.ui.prodLevelLineEdit.setText(str(self._production_rate))
        self.ui.employeeLineEdit.setText(str(self._employees))
        self.ui.prodOnCheckBox.setChecked(self._production_on)
    
    def on_turn_end(self, turn_number):
        if self.production_on:
            self.change_primitive_resource.emit("Food", self.production_rate)
    
    #Properties and UI updaters
    @pyqtProperty(int)
    def production_rate(self):
        return self._production_rate
    
    @production_rate.setter
    def production_rate(self, value):
        self._production_rate = value
        self.ui.prodLevelLineEdit.setText(str(self._production_rate))
    
    @pyqtProperty(int)
    def employees(self):
        return self._employees
    
    @employees.setter
    def employees(self, value):
        self._employees = value
        self.ui.employeeLineEdit.setText(str(self._employees))
    
    @pyqtProperty(bool)
    def production_on(self):
        return self._production_on
    
    @production_on.setter
    def production_on(self, value):
        self._production_on = value
        self.ui.prodOnCheckBox.setChecked(self._production_on)
    
    @pyqtSlot(bool)
    def production_on_checked(self, checked):
        self._production_on = checked
