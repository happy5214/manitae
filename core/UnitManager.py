import pkgutil

from PyQt4 import QtCore, QtGui

from ManitaeGame import *
from Producer import *
from TurnManager import *
from Unit import *

from OutOfMoneyError import *

import units

class UnitManager(QtCore.QObject):
    def __init__(self, game):
        super(UnitManager, self).__init__()
        self.game = game
        self.turn_manager = self.game.turn_manager
        self.setup_unit_types()
        self.units = []
        self.unit_type_model = QtGui.QStringListModel(self.unit_types)
        Unit.id_inc = 1
    
    def build(self, unit_to_build):
        unit_to_build_clean = unit_to_build.replace(' ', '')
        unit = eval("units.{0}.{0}()".format(unit_to_build_clean))
        self.turn_manager.turn_ended.connect(unit.on_turn_end)
        try:
            self.game.economy_manager.build(unit)
        except OutOfMoneyError as e:
            del unit
            raise e
        if isinstance(unit, Producer):
            unit.change_primitive_resource.connect(self.game.resource_manager.update_primitive_resource)
            unit.employee_fired.connect(self.fire_employee)
            unit.employee_hired.connect(self.hire_employee)
            unit.needs_employee.connect(self.game.population_manager.allocate_employee_to_unit)
            unit.to_be_destroyed.connect(self.destroy_unit)
            try:
                unit.ready_for_allocation()
            except NoMoreWorkersError as e:
                del unit
                raise e
        unit.name_changed_sig.connect(self.unit_name_changed)
        self.units.append(unit)
        self.game.logger.append_notice("{0} built.".format(unit.UNIT))
        self.game.add_tab(unit.widget, unit.UNIT)
    
    def setup_unit_types(self):
        self.unit_types = []
        for x in pkgutil.walk_packages(['units']):
            if not(x[1].startswith('ui_')):
                __import__("units." + x[1])
                self.unit_types.append(eval("units." + x[1] + '.' + x[1] + ".UNIT"))
    
    def fire_employee(self, emp_str):
        unit = self.sender()
        emp = self.game.population_manager.str_to_person[str(emp_str)]
        emp.employer = None
        unit.employees.remove(emp)
        self.game.population_manager.employee_fired(1)
        if unit.employee_count == 0:
            unit.production_on = False
    
    def hire_employee(self, emp_str):
        unit = self.sender()
        emp = self.game.population_manager.str_to_person[str(emp_str)]
        emp.employer = unit
        unit.employees.append(emp)
        self.game.population_manager.employee_hired(1)
        if unit.employee_count == unit.employee_max:
            unit.production_on = True
    
    def destroy_unit(self):
        unit = self.sender()
        widget = unit.widget
        for p in unit.employees:
            p.employer = None
        self.game.population_manager.employee_fired(len(unit.employees))
        self.units.remove(unit)
        self.game.main_window.ui.tabWidget.removeTab(self.game.main_window.ui.tabWidget.indexOf(widget))
        self.game.logger.append_notice("{0} destroyed.".format(unit.UNIT))
        del unit
    
    def unit_name_changed(self):
        self.game.main_window.ui.tabWidget.setTabText(self.game.main_window.ui.tabWidget.indexOf(self.sender().widget), self.sender().name)
