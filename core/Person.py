from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal, pyqtProperty, pyqtSlot

from core.Unit import Unit

from people.ui_Person import Ui_Person

class Person(QtCore.QObject):
    
    TYPE = "Person"
    level = -1
    id_inc = 1
    
    name_changed_sig = pyqtSignal()
    
    def __init__(self):
        super(Person, self).__init__()
        self._employer = None
        self.id = Person.id_inc
        Person.id_inc += 1
        self._total_expenses = 0.0
        self._net_worth = 0.0
        self._name = ''
        self.shelter = None
        
        self.ui = Ui_Person()
        self.widget = QtGui.QWidget()
        self.ui.setupUi(self.widget)
        
        self.ui.nameLineEdit.textEdited.connect(self.name_changed)
        self.ui.typeLineEdit.setText(self.TYPE)
        self.ui.levelLineEdit.setText(str(self.level))
        self.ui.netWorthLineEdit.setText(self.display_money(self._net_worth))
    
    def __str__(self):
        if not(self.name):
            return "{0} (Level {1}): id {2}".format(self.TYPE, self.level, str(self.id))
        else:
            return self.name
    
    def key(self):
        return self.level
    
    @pyqtProperty(Unit)
    def employer(self):
        return self._employer
    
    @employer.setter
    def employer(self, unit):
        self._employer = unit
        self.ui.employerLineEdit.setText(str(self._employer))
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.ui.taxesLineEdit.setText(self.display_money(self.income_tax))
        self.ui.netLineEdit.setText(self.display_money(self.net))
    
    @pyqtProperty(str)
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        self.name_changed_sig.emit()
    
    @pyqtProperty(float)
    def net_worth(self):
        return self._net_worth
    
    @net_worth.setter
    def net_worth(self, value):
        self._net_worth = value
        self.ui.netWorthLineEdit.setText(self.display_money(self._net_worth))
    
    @pyqtProperty(float)
    def income_tax(self):
        if self.shelter:
            pass
        else:
            return self.salary * 0.05
    
    @pyqtProperty(float)
    def salary(self):
        try:
            return self._employer.get_salary(self)
        except AttributeError:
            return 0.0
    
    @pyqtProperty(float)
    def net(self):
        return self.total_income - self.total_expenses
    
    @pyqtProperty(float)
    def total_expenses(self):
        return self.income_tax
    
    @pyqtProperty(float)
    def total_income(self):
        return self.salary
    
    def employer_production_switched(self):
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.ui.taxesLineEdit.setText(self.display_money(self.income_tax))
        self.ui.netLineEdit.setText(self.display_money(self.net))
    
    def name_changed(self, new_name):
        self.name = str(new_name)
    
    def on_turn_end(self):
        self.net_worth += self.net
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.ui.taxesLineEdit.setText(self.display_money(self.income_tax))
        self.ui.netLineEdit.setText(self.display_money(self.net))
    
    def display_money(self, amount):
        return "{:.2f}".format(amount)
    
