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

import pkgutil

from PyQt4 import QtCore, QtGui

from manitae.core.basetypes.Unit import *

from manitae.errors.NoMoreWorkersError import NoMoreWorkersError
from manitae.errors.OutOfMoneyError import OutOfMoneyError

from manitae.maps.MapTile import MapTile

from manitae.units.base.Producer import Producer

import manitae.units

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
        unit.coords = self.game.map_manager.current_tile_coords
        unit.tile = self.game.map_manager.current_tile
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
        unit.send_notice.connect(self.game.logger.append_notice)
        unit.send_warning.connect(self.game.logger.append_warning)
        self.units.append(unit)
        self.game.map_manager.current_tile.unit = unit
        index = self.game.map_manager.model.index(self.game.map_manager.model.coords_to_index(unit.coords), 0)
        self.game.map_manager.model.dataChanged.emit(index, index)
        self.game.logger.append_notice("{0} built.".format(str(unit)))
        self.game.add_tab(unit.widget, str(unit))
        return unit
    
    def setup_unit_types(self):
        """Sets up the population_types list."""
        unit_types = self.game.scenario.register_unit_types()
        if not(unit_types):
            for x in pkgutil.walk_packages(['units']):
                if not(x[1].startswith('ui_')):
                    __import__("units." + x[1])
                    self.unit_types.append(eval("units." + x[1] + '.' + x[1] + ".UNIT"))
        else:
            self.unit_types = unit_types
            for x in self.unit_types:
                __import__("units." + x.replace(' ', ''))
    
    def setup_basic_units(self):
        self.game.scenario.setup_basic_units(self)
    
    def fire_employee(self, emp_str):
        unit = self.sender()
        emp = self.game.population_manager.str_to_person[str(emp_str)]
        emp.employer = None
        unit.employees.remove(emp)
        self.game.population_manager.employee_fired(1)
        if unit.employee_count == 0:
            unit.production_on = False
        self.game.logger.append_notice("{0} fired employee {1}.".format(str(unit), emp_str))
    
    def hire_employee(self, emp_str):
        unit = self.sender()
        emp = self.game.population_manager.str_to_person[str(emp_str)]
        emp.employer = unit
        unit.employees.append(emp)
        self.game.population_manager.employee_hired(1)
        if unit.employee_count == unit.employee_max:
            unit.production_on = True
        self.game.logger.append_notice("{0} hired employee {1}.".format(str(unit), emp_str))
    
    def destroy_unit(self):
        unit = self.sender()
        widget = unit.widget
        for p in unit.employees:
            p.employer = None
        self.game.population_manager.employee_fired(len(unit.employees))
        self.units.remove(unit)
        self.game.main_window.ui.tabWidget.removeTab(self.game.main_window.ui.tabWidget.indexOf(widget))
        self.game.logger.append_notice("{0} destroyed.".format(str(unit)))
        coords = unit.coords
        tile = unit.tile
        tile.unit = None
        tile.__class__ = tile.tile_type
        del unit
        index = self.game.map_manager.model.index(self.game.map_manager.model.coords_to_index(coords), 0)
        self.game.map_manager.model.dataChanged.emit(index, index)
        self.game.map_manager.update_data(coords, tile)
    
    def unit_name_changed(self):
        self.game.main_window.ui.tabWidget.setTabText(self.game.main_window.ui.tabWidget.indexOf(self.sender().widget), str(self.sender()))
