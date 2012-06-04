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

from manitae.maps.MapTile import MapTile

from manitae.units.base.LevelOnePrimitiveProducer import LevelOnePrimitiveProducer
from manitae.units.base.SingleTileUnit import SingleTileUnit

from ui_PrimitiveProducer import Ui_PrimitiveProducer

class StoneGathererTile(MapTile):
    """:class:`~maps.MapTile.MapTile` type for :class:`StoneGatherer`"""
    buildable = False
    tile = "./tile_images/units/StoneGatherer/StoneGatherer32.png"
    def __init__(self, color):
        super(StoneGathererTile, self).__init__(color)
    

class StoneGatherer(LevelOnePrimitiveProducer, SingleTileUnit):
    """:class:`~units.base.LevelOnePrimitiveProducer.LevelOnePrimitiveProducer` that produces :class:`~resources.Stone.Stone`
    
    This unit type...
    
    * costs N20.00 to construct.
    * employs one person of the types :class:`~people.Citizen.Citizen` and :class:`~people.StoneGatherer.StoneGatherer`
    * produces 2 :class:`~resources.Stone.Stone` when employing a :class:`~people.Citizen.Citizen`, at a salary of N7.50.
    * produces 3 :class:`~resources.Stone.Stone` when employing a :class:`~people.StoneGatherer.StoneGatherer`, at a salary of N10.00.
    * provides 1 unit of experience of type StoneGatherer upon completion of 1 turn of work.
    * occupies a single tile."""
    
    UNIT = "Stone Gatherer"
    tile_type = StoneGathererTile
    level = 1
    
    employee_types = ['Citizen', 'Stone Gatherer']
    employee_efficiency = {'Citizen': 2, 'Stone Gatherer': 3}
    employee_salary = {'Citizen': 7.50, 'Stone Gatherer': 10.00}
    employee_max = 1
    
    construction_cost = 20
    
    def __init__(self):
        super(StoneGatherer, self).__init__()
        
    def on_turn_end(self, turn_number):
        if self.production_on:
            self.change_primitive_resource.emit("Stone", self.production_rate)
            self.employees[0].gain_experience("Stone Gatherer", 1)
    
