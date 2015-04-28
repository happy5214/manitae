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

from PyQt4 import QtGui, QtCore

from manitae.core.managers.EconomyManager import EconomyManager
from manitae.core.managers.ManitaeLogger import ManitaeLogger
from manitae.core.managers.MapManager import MapManager
from manitae.core.managers.PopulationManager import PopulationManager
from manitae.core.managers.ResourceManager import ResourceManager
from manitae.core.managers.ScenarioManager import ScenarioManager
from manitae.core.managers.TurnManager import TurnManager
from manitae.core.managers.UnitManager import UnitManager

from manitae.errors.NoMoreWorkersError import NoMoreWorkersError
from manitae.errors.OutOfMoneyError import OutOfMoneyError

class ManitaeGame(QtCore.QObject):
    def __init__(self, main_window):
        super(ManitaeGame, self).__init__()
        self.main_window = main_window
        
        self.scenario_manager = ScenarioManager(self)
        self.scenario = self.scenario_manager.get_scenario()
        
        self.logger = ManitaeLogger()
        self.logger.send_entry.connect(self.add_log_entry)
        self.logger.append_notice("New game started.")
        
        self.turn_manager = TurnManager(self)
        self.map_manager = MapManager(self)
        
        self.economy_manager = EconomyManager(self)
        self.population_manager = PopulationManager(self)
        self.resource_manager = ResourceManager(self)
        self.unit_manager = UnitManager(self)
        
        self.turn_manager.turn_ended.connect(self.economy_manager.on_turn_end)
        
        self.extra_tabs = []
        
        self.main_window.ui.widget.ui.resourceComboBox.setModel(self.resource_manager.resource_type_model)
        self.main_window.ui.widget.ui.resourceComboBox.activated[str].connect(self.update_resource_widget)
        self.main_window.ui.buildComboBox.setModel(self.unit_manager.unit_type_model)
        self.main_window.ui.buildComboBox.setItemIcon(self.main_window.ui.buildComboBox.findText("Hunter"), QtGui.QIcon("./manitae/maps/tile_images/units/Hunter/Hunter.svg"))
        self.main_window.ui.buildPushButton.clicked.connect(self.build)
        
        self.resource_manager.resource_changed.connect(self.update_resource_widget_after_turn)
        
        self.main_window.ui.widget.ui.resourceLineEdit.setText('0')
    
    def add_log_entry(self, log_entry):
        temp_cursor = self.main_window.ui.noticeLog.textCursor()
        temp_cursor.movePosition(QtGui.QTextCursor.End)
        self.main_window.ui.noticeLog.setTextCursor(temp_cursor)
        self.main_window.ui.noticeLog.insertHtml(log_entry)
    
    def add_tab(self, tab, name):
        tab_number = self.main_window.ui.tabWidget.addTab(tab, name)
        self.extra_tabs.append(tab)
        return tab_number
    
    def build(self):
        unit_str = self.main_window.ui.buildComboBox.currentText()
        try:
            unit = self.unit_manager.build(unit_str)
            self.main_window.ui.goToTabPushButton.setEnabled(True)
            self.main_window.ui.tileOccupantLineEdit.setText(str(unit))
            self.main_window.ui.buildPushButton.setEnabled(unit.tile.buildable)
        except (NoMoreWorkersError, OutOfMoneyError) as e:
            self.logger.append_warning(str(e))
    
    def end_turn(self):
        self.turn_manager.end_turn()
    
    def restart_game(self):
        
        scenario_manager = ScenarioManager(self)
        scenario = scenario_manager.get_scenario()
        
        del self.scenario_manager
        del self.scenario
        self.scenario_manager = scenario_manager
        self.scenario = scenario
        
        for x in self.extra_tabs:
            self.main_window.ui.tabWidget.removeTab(self.main_window.ui.tabWidget.indexOf(x))
        del self.extra_tabs
        del self.economy_manager
        del self.map_manager
        del self.population_manager
        del self.resource_manager
        del self.turn_manager
        del self.unit_manager
        #
        
        self.logger.append_notice("New game started.")
        self.turn_manager = TurnManager(self)
        self.map_manager = MapManager(self)
        
        self.economy_manager = EconomyManager(self)
        self.population_manager = PopulationManager(self)
        self.resource_manager = ResourceManager(self)
        self.unit_manager = UnitManager(self)
        
        self.turn_manager.turn_ended.connect(self.economy_manager.on_turn_end)
        
        self.extra_tabs = []
        
        self.main_window.ui.widget.ui.resourceComboBox.setModel(self.resource_manager.resource_type_model)
        self.main_window.ui.widget.ui.buildComboBox.setModel(self.unit_manager.unit_type_model)
        self.main_window.ui.buildComboBox.setItemIcon(self.main_window.ui.buildComboBox.findText("Hunter"), QtGui.QIcon("./manitae/maps/tile_images/units/Hunter/Hunter.svg"))
        
        self.resource_manager.resource_changed.connect(self.update_resource_widget_after_turn)
        
        self.main_window.ui.widget.ui.resourceLineEdit.setText('0')
    
    def update_resource_widget(self, resource):
        res_amount = self.resource_manager.resources[str(resource)]
        self.main_window.ui.widget.ui.resourceLineEdit.setText(str(res_amount))
    
    def update_resource_widget_after_turn(self, resource_changed):
        resource = self.main_window.ui.widget.ui.resourceComboBox.currentText()
        if resource == resource_changed:
            res_amount = self.resource_manager.resources[str(resource)]
            self.main_window.ui.widget.ui.resourceLineEdit.setText(str(res_amount))
