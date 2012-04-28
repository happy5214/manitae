#   Copyright (C) 2012 Alexander Jones
#
#   This file is part of Manitae.
#
#   Manitae is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Manitae is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Manitae.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtCore import pyqtSignal, pyqtProperty, pyqtSlot, QObject
from PyQt4.QtGui import QWidget, QStringListModel, QMessageBox

from core.Unit import Unit

import people
from people.ui_Person import Ui_Person

class Person(QObject):
    
    TYPE = "Person"
    level = -1
    id_inc = 1
    level_up_types = []
    
    name_changed_sig = pyqtSignal()
    send_notice = pyqtSignal(str)
    send_warning = pyqtSignal(str)
    upgraded = pyqtSignal()
    
    def __init__(self):
        super(Person, self).__init__()
        self._employer = None
        self.id = Person.id_inc
        Person.id_inc += 1
        self._total_expenses = 0.0
        self._net_worth = 0.0
        self._name = ''
        self.experience = {}
        self.shelter = None
        self.level_up_type_model = QStringListModel(self.level_up_types)
        self.exp_type_model = QStringListModel(self.exp_types)
        
        self.ui = Ui_Person()
        self.widget = QWidget()
        self.ui.setupUi(self.widget)
        
        self.ui.upgradeComboBox.setModel(self.level_up_type_model)
        self.ui.upgradePushButton.clicked.connect(self.upgrade)
        self.ui.expComboBox.setModel(self.exp_type_model)
        self.ui.expComboBox.activated[str].connect(self.update_experience_widget)
        self.ui.nameLineEdit.textEdited.connect(self.name_changed)
        self.ui.typeLineEdit.setText(self.TYPE)
        self.ui.levelLineEdit.setText(str(self.level))
        self.ui.employerLineEdit.setText("Unemployed")
        self.ui.netWorthLineEdit.setText(self.display_money(self._net_worth))
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.ui.totalIncomeLineEdit.setText(self.display_money(self.total_income))
        self.ui.taxesLineEdit.setText(self.display_money(self.income_tax))
        self.ui.netLineEdit.setText(self.display_money(self.net))
    
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
        self.ui.employerLineEdit.setText(str(self._employer) if self._employer else "Unemployed")
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.ui.totalIncomeLineEdit.setText(self.display_money(self.total_income))
        self.ui.taxesLineEdit.setText(self.display_money(self.income_tax))
        self.ui.netLineEdit.setText(self.display_money(self.net))
    
    @pyqtProperty(list)
    def exp_types(self):
        return self.experience.keys()
    
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
            return self._employer.emp_to_salary[self]
        except (AttributeError, KeyError):
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
        self.ui.totalIncomeLineEdit.setText(self.display_money(self.total_income))
        self.ui.taxesLineEdit.setText(self.display_money(self.income_tax))
        self.ui.netLineEdit.setText(self.display_money(self.net))
    
    def name_changed(self, new_name):
        self.name = str(new_name)
    
    def on_turn_end(self):
        self.net_worth += self.net
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.ui.totalIncomeLineEdit.setText(self.display_money(self.total_income))
        self.ui.taxesLineEdit.setText(self.display_money(self.income_tax))
        self.ui.netLineEdit.setText(self.display_money(self.net))
    
    def gain_experience(self, exp_type, amount):
        try:
            self.experience[exp_type] += amount
        except KeyError:
            self.experience[exp_type] = amount
            self.exp_type_model.setStringList(self.exp_types)
        finally:
            self.update_experience_widget_after_turn(exp_type)
    
    def upgrade(self):
        person_type = self.ui.upgradeComboBox.currentText()
        if not(person_type):
            return
        person_type_clean = person_type.replace(' ', '')
        upgrade_check, error = eval("people.{0}.{0}.upgrade_to(self)".format(person_type_clean))
        if not(upgrade_check):
            self.send_warning.emit("Could not upgrade person {0}: {1}".format(str(self), error))
        else:
            self.name_changed_sig.emit()
            self.upgraded.emit()
            self.employer.employee_upgraded(self)
    
    def update_experience_widget(self, exp_type):
        exp_amount = self.experience[str(exp_type)]
        self.ui.expLineEdit.setText(str(exp_amount))
    
    def update_experience_widget_after_turn(self, exp_changed):
        exp_type = self.ui.expComboBox.currentText()
        if str(exp_type) == str(exp_changed):
            exp_amount = self.experience[str(exp_type)]
            self.ui.expLineEdit.setText(str(exp_amount))
    
    def display_money(self, amount):
        return "{:.2f}".format(amount)
    
