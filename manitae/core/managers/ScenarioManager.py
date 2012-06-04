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

from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import QDialog

from manitae.core.basetypes.Scenario import Scenario

from manitae.errors.NoScenarioSelectedError import NoScenarioSelectedError

import manitae.scenarios

class ScenarioManager(QtCore.QObject):
    def __init__(self, game):
        super(ScenarioManager, self).__init__()
        self.game = game
        self.import_scenarios()
        self.scenario_dialog = QDialog(self.game.main_window)
        uic.loadUi('./manitae/core/ui/ScenarioDialog.ui', self.scenario_dialog)
    
    def import_scenarios(self):
        self.available_scenarios = []
        self.name_to_class = {}
        for x in pkgutil.walk_packages(['manitae/scenarios']):
            if not(x[1].startswith('ui_')):
                __import__("manitae.scenarios." + x[1])
                name = eval("manitae.scenarios." + x[1] + '.' + x[1] + ".NAME")
                self.available_scenarios.append(name)
                self.name_to_class[name] = x[1]
        self.scenario_config_widgets = {}
        for n, c in self.name_to_class.items():
            w = eval("manitae.scenarios.{0}.{0}.get_config_widget()".format(c))
            self.scenario_config_widgets[n] = w
        self.scenario_list_model = QtGui.QStringListModel()
        self.scenario_list_model.setStringList(self.available_scenarios)
    
    def get_scenario(self):
        self.scenario_dialog.comboBox.setModel(self.scenario_list_model)
        self.scenario_dialog.comboBox.activated[str].connect(self.update_scenario_dialog_widget)
        self.active_widget = None
        self.update_scenario_dialog_widget(self.scenario_dialog.comboBox.currentText(), True)
        result = self.scenario_dialog.exec_()
        if result == QDialog.Accepted:
            name = self.scenario_dialog.comboBox.currentText()
            if not(name):
                raise NoScenarioSelectedError()
            widget = self.active_widget
            c = self.name_to_class[str(name)]
            self.scenario = eval("manitae.scenarios.{0}.{0}(self.game, widget)".format(c))
            return self.scenario
        else:
            raise NoScenarioSelectedError()
    
    def update_scenario_dialog_widget(self, scenario_str, first = False):
        new_active_widget = self.scenario_config_widgets[str(scenario_str)]
        if self.active_widget != new_active_widget:
            if not(first):
                self.scenario_dialog.widget.layout().removeWidget(self.active_widget)
            self.scenario_dialog.widget.layout().addWidget(new_active_widget)
            self.active_widget = new_active_widget
            self.scenario_dialog.update()
    
