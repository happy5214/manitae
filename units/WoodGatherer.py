from PyQt4.QtCore import pyqtSignal, pyqtProperty, pyqtSlot
from PyQt4.QtGui import QWidget, QStringListModel, QMessageBox

from core.Producer import *
from ui_WoodGatherer import Ui_WoodGatherer

class WoodGatherer(Producer):
    
    UNIT = "Wood Gatherer"
    
    employee_types = ['Citizen', 'Wood Gatherer']
    employee_efficiency = {'Citizen': 2, 'Wood Gatherer': 3}
    employee_salary = {'Citizen': 7.50, 'Wood Gatherer': 10.00}
    employee_max = 1
    
    construction_cost = 20
    
    def __init__(self):
        super(WoodGatherer, self).__init__()
        self.employees = []
        self._production_on = False
        self.employee_model = QStringListModel()
        self.hirable_model = QStringListModel()
        
        self.ui = Ui_WoodGatherer()
        self.widget = QWidget()
        self.ui.setupUi(self.widget)
        
        self.ui.fireComboBox.setModel(self.employee_model)
        self.ui.fireButton.clicked.connect(self.fire_employee)
        self.ui.hireComboBox.setModel(self.hirable_model)
        self.ui.hireButton.clicked.connect(self.hire_employee)
        self.ui.prodOnCheckBox.toggled.connect(self.production_on_checked)
        self.ui.employeeLineEdit.setText(str(self.employee_count))
        self.ui.prodOnCheckBox.setChecked(self.production_on)
        self.ui.destroyButton.clicked.connect(self.destroy)
        self.ui.employeeListView.setModel(self.employee_model)
    
    def on_turn_end(self, turn_number):
        if self.production_on:
            self.change_primitive_resource.emit("Wood", self.production_rate)
    
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
        return self.employee_efficiency[self.employees[0].TYPE]
    
    @pyqtProperty(float)
    def salary(self):
        if self.production_on:
            return self.employee_salary[self.employees[0].TYPE]
        else:
            return 0.0
    
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
        except IndexError as e:
            pass
    
    @pyqtSlot(bool)
    def production_on_checked(self, checked):
        self.production_on = checked
    
    def destroy(self):
        self.to_be_destroyed.emit()
    
    def fire_employee(self):
        if self.employee_count == 0:
            QMessageBox.warning(self.widget, "Unable to fire employee", "This unit has no employees.")
            return
        emp_str = self.ui.fireComboBox.currentText()
        self.employee_fired.emit(emp_str)
        self.ui.employeeLineEdit.setText(str(self.employee_count))
        self.employee_model.setStringList(self.employee_string_list)
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
    
    def hire_employee(self):
        if self.employee_count == self.employee_max:
            QMessageBox.warning(self.widget, "Unable to hire employee", "This unit has the maximum number of employees.")
            return
        emp_str = self.ui.hireComboBox.currentText()
        self.employee_hired.emit(emp_str)
        self.ui.employeeLineEdit.setText(str(self.employee_count))
        self.employee_model.setStringList(self.employee_string_list)
        self.ui.salaryLineEdit.setText(self.display_money(self.salary))
