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

from core.LevelOnePrimitiveProducer import *
from core.SingleTileUnit import SingleTileUnit
from maps.MapTile import *
from ui_PrimitiveProducer import Ui_PrimitiveProducer

class GathererTile(MapTile):
    """:class:`maps.MapTile.MapTile` type for :class:`Gatherer`"""
    buildable = False
    tile = "./tiles/units/Gatherer/Gatherer32.png"
    def __init__(self, color):
        super(GathererTile, self).__init__(color)
    

class Gatherer(LevelOnePrimitiveProducer, SingleTileUnit):
    """:class:`core.LevelOnePrimitiveProducer.LevelOnePrimitiveProducer` that produces :class:`resources.Food.Food`
    
    This unit type...
    * costs N20.00 to construct.
    * employs one person of the types :class:`people.Citizen.Citizen` and :class:`people.Gatherer.Gatherer`
    * produces 2 :class:`resources.Food.Food` when employing a :class:`people.Citizen.Citizen`, at a salary of N7.50.
    * produces 3 :class:`resources.Food.Food` when employing a :class:`people.Gatherer.Gatherer`, at a salary of N10.00.
    * provides 1 unit of experience of type Gatherer upon completion of 1 turn of work.
    * occupies a single tile."""
    
    UNIT = "Gatherer"
    tile_type = GathererTile
    level = 1
    
    employee_types = ['Citizen', 'Gatherer']
    employee_efficiency = {'Citizen': 2, 'Gatherer': 3}
    employee_salary = {'Citizen': 7.50, 'Gatherer': 10.00}
    employee_max = 1
    
    construction_cost = 20
    
    def __init__(self):
        super(Gatherer, self).__init__()
    
    def on_turn_end(self, turn_number):
        if self.production_on:
            self.change_primitive_resource.emit("Food", self.production_rate)
            self.employees[0].gain_experience("Gatherer", 1)
    
