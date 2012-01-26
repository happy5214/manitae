import pkgutil

from PyQt4 import QtCore, QtGui

from ManitaeGame import *
from TurnManager import *
from Unit import *

import units

class UnitManager(QtCore.QObject):
    def __init__(self, game):
        super(UnitManager, self).__init__()
        self.game = game
        self.turn_manager = self.game.turn_manager
        self.setup_unit_types()
        self.units = []
        self.unit_type_model = QtGui.QStringListModel(self.unit_types)
    
    def build(self, unit_to_build):
        unit = eval("units.{0}.{0}()".format(unit_to_build))
        self.turn_manager.turn_ended.connect(unit.on_turn_end)
        unit.change_primitive_resource.connect(self.game.resource_manager.update_primitive_resource)
        self.units.append(unit)
        self.game.logger.append_notice("{0} built.".format(unit_to_build))
        self.game.add_tab(unit.widget, unit_to_build)
    
    def setup_unit_types(self):
        self.unit_types = []
        for x in pkgutil.walk_packages(['units']):
            if not(x[1].startswith('ui_')):
                self.unit_types.append(x[1])
        for x in self.unit_types:
            __import__("units." + x)
        
