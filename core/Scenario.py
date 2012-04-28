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

from PyQt4 import QtCore

class Scenario(QtCore.QObject):
    def __init__(self, game):
        super(Scenario, self).__init__()
        self.game = game
    
    def register_person_types(self):
        return self.person_types
    
    def register_resource_types(self):
        return self.resource_types
    
    def register_unit_types(self):
        return self.unit_types
    
    def setup_basic_units(self, manager):
        return False
    
    def setup_basic_population(self, manager):
        return False
    
