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

from PyQt4.QtCore import pyqtSignal, pyqtProperty, pyqtSlot
from PyQt4.QtGui import QWidget, QStringListModel, QMessageBox

from manitae.errors.NoMoreWorkersError import NoMoreWorkersError

from manitae.units.base.PrimitiveProducer import PrimitiveProducer
from manitae.units.ui_PrimitiveProducer import Ui_PrimitiveProducer

class LevelOnePrimitiveProducer(PrimitiveProducer):
    """A :class:`~units.base.PrimitiveProducer.PrimitiveProducer` at :attr:`~core.basetypes.Unit.Unit.level` 1
    
    Level 1 Primitive Producers include (in the base package):
    
    * :class:`~units.Gatherer.Gatherer`
    * :class:`~units.Hunter.Hunter`
    * :class:`~units.StoneGatherer.StoneGatherer`
    * :class:`~units.WoodGatherer.WoodGatherer`
    """
    
    level = 1
    
    employee_types = ['Citizen']
    """Types of :class:`people <core.basetypes.Person.Person>` that may be employed by this unit."""
    employee_efficiency = {'Citizen': 2}
    """Production rate per type of employee."""
    employee_salary = {'Citizen': 7.50}
    """Salary per type of employee."""
    employee_max = 1
    """Maximum number of people that can be employed at one time."""
    
    def __init__(self):
        super(LevelOnePrimitiveProducer, self).__init__()
        self.employees = []
        self._production_on = False
        self.employee_model = QStringListModel()
        self.hirable_model = QStringListModel()
        
        self.ui = Ui_PrimitiveProducer()
        self.widget = QWidget()
        self.ui.setupUi(self.widget)
        
        self.ui.typeLineEdit.setText(self.UNIT)
        self.ui.levelLineEdit.setText(str(self.level))
        self.ui.nameLineEdit.textEdited.connect(self.name_changed)
        self.ui.fireComboBox.setModel(self.employee_model)
        self.ui.fireButton.clicked.connect(self.fire_employee)
        self.ui.hireComboBox.setModel(self.hirable_model)
        self.ui.hireButton.clicked.connect(self.hire_employee)
        self.ui.prodOnCheckBox.toggled.connect(self.production_on_checked)
        self.ui.employeeLineEdit.setText(str(self.employee_count))
        self.ui.prodOnCheckBox.setChecked(self.production_on)
        self.ui.destroyButton.clicked.connect(self.destroy)
        self.ui.employeeListView.setModel(self.employee_model)
    
    def ready_for_allocation(self):
        self.needs_employee.emit(self, 1)
        if self.employee_count == 0:
            raise NoMoreWorkersError(self.UNIT)
        self.employee_model.setStringList(self.employee_string_list)
        self.ui.employeeLineEdit.setText(str(self.employee_count))
        self.ui.prodLevelLineEdit.setText(str(self.production_rate))
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.production_on = True
    
    #Properties and UI updaters
    
    @pyqtProperty(list)
    def employee_string_list(self):
        string_list = []
        for x in self.employees:
            string_list.append(str(x))
        return string_list
    
    @pyqtProperty(int)
    def production_rate(self):
        try:
            if self.production_on:
                return self.employee_efficiency[self.employees[0].TYPE]
            else:
                return 0
        except (IndexError, KeyError):
            return 0
    
    @pyqtProperty(float)
    def salary(self):
        try:
            if self.production_on:
                return self.employee_salary[self.employees[0].TYPE]
            else:
                return 0.0
        except (IndexError, KeyError):
            return 0.0
    
    @pyqtProperty(dict)
    def emp_to_salary(self):
        try:
            if self.production_on:
                return {self.employees[0]: self.employee_salary[self.employees[0].TYPE]}
            else:
                return {self.employees[0]: 0.0}
        except IndexError:
            return {}
    
    @pyqtProperty(int)
    def employee_count(self):
        return len(self.employees)
    
    @pyqtProperty(bool)
    def production_on(self):
        return self._production_on
    
    @production_on.setter
    def production_on(self, value):
        self._production_on = value
        self.ui.prodOnCheckBox.setChecked(self._production_on)
        try:
            self.salary_changed.emit(self.salary)
            self.ui.salaryLineEdit.setText(self.display_money(self.salary))
            self.ui.prodLevelLineEdit.setText(str(self.production_rate))
            for emp in self.employees:
                emp.employer_production_switched()
            self.production_switched.emit()
        except IndexError:
            pass
    
    @pyqtSlot(bool)
    def production_on_checked(self, checked):
        self.production_on = checked
    
    def destroy(self):
        self.production_on = False
        self.to_be_destroyed.emit()
    
    def fire_employee(self):
        if self.employee_count == 0:
            self.send_warning.emit("Unable to fire employee from unit {0}: this unit has no employees.".format(str(self)))
            return
        emp_str = self.ui.fireComboBox.currentText()
        self.employee_fired.emit(emp_str)
        self.ui.employeeLineEdit.setText(str(self.employee_count))
        self.employee_model.setStringList(self.employee_string_list)
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.ui.prodLevelLineEdit.setText(str(self.production_rate))
    
    def hire_employee(self):
        if self.employee_count == self.employee_max:
            self.send_warning.emit("Unable to hire employee for unit {0}: this unit has the maximum number of employees.".format(str(self)))
            return
        emp_str = self.ui.hireComboBox.currentText()
        self.employee_hired.emit(emp_str)
        self.ui.employeeLineEdit.setText(str(self.employee_count))
        self.employee_model.setStringList(self.employee_string_list)
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
        self.ui.prodLevelLineEdit.setText(str(self.production_rate))
    
    def employee_upgraded(self, emp):
        if (emp.TYPE not in self.employee_types):
            emp_str = str(emp)
            self.employee_fired.emit(emp_str)
            self.ui.employeeLineEdit.setText(str(self.employee_count))
            self.employee_model.setStringList(self.employee_string_list)
            self.ui.salaryLineEdit.setText(self.display_money(self.salary))
            self.ui.prodLevelLineEdit.setText(str(self.production_rate))
        else:
            self.ui.salaryLineEdit.setText(self.display_money(self.salary))
            self.ui.prodLevelLineEdit.setText(str(self.production_rate))
            self.salary_changed.emit(self.salary)
    
    def name_changed(self, new_name):
        self.name = str(new_name)
        self.employees[0].ui.employerLineEdit.setText(str(self))
    
