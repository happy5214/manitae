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

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QWidget

from core.Scenario import *

from maps.MapTile import *

from people.Citizen import *

class TheBasics(Scenario):
    
    NAME = "The Basics"
    
    person_types = ["Citizen", "Gatherer", "Hunter", "StoneGatherer", "WoodGatherer"]
    resource_types = ["Food", "Stone", "Wood"]
    unit_types = ["Gatherer", "Hunter", "Stone Gatherer", "Wood Gatherer"]
    
    def __init__(self, game, widget):
        super(TheBasics, self).__init__(game)
        self.tutorial_mode = widget.tutorialCheckBox.isChecked()
    
    @staticmethod
    def get_config_widget():
        return uic.loadUi('./scenarios/ui/TheBasicsConfig.ui')
    
    def setup_basic_population(self, manager):
        for x in range(5):
            manager.register_person(Citizen)
        return True
    
    def setup_map(self):
        size = 100
        map_data = []
        top = []
        top.append(MapTile("green", "./tiles/roads/path1/32px/downright.png"))
        top.append(MapTile("green", "./tiles/roads/path1/32px/downleft.png"))
        top.append(MapTile("green", ""))
        top.append(MapTile("green", "./tiles/roads/path1/32px/downright.png"))
        for y in range(size - 5):
            top.append(MapTile("green", "./tiles/roads/path1/32px/horizdown.png"))
        top.append(MapTile("green", "./tiles/roads/path1/32px/downleft.png"))
        map_data.append(top)
        for x in range(size - 2):
            r = []
            r.append(MapTile("green", "./tiles/roads/path1/32px/vertright.png"))
            for y in range(size - 2):
                r.append(MapTile("green", "./tiles/roads/path1/32px/cross.png"))
            r.append(MapTile("green", "./tiles/roads/path1/32px/vertleft.png"))
            map_data.append(r)
        bottom = []
        bottom.append(MapTile("green", "./tiles/roads/path1/32px/upright.png"))
        for y in range(size - 2):
            bottom.append(MapTile("green", "./tiles/roads/path1/32px/horizup.png"))
        bottom.append(MapTile("green", "./tiles/roads/path1/32px/upleft.png"))
        map_data.append(bottom)
        return map_data
