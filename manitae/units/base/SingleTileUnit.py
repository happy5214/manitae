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

from PyQt4.QtCore import pyqtProperty

from manitae.core.basetypes.Unit import Unit
from manitae.maps.MapTile import MapTile

class SingleTileUnit(Unit):
    
    tile_type = MapTile
    
    @pyqtProperty(MapTile)
    def tile(self):
        return self._tile
    
    @tile.setter
    def tile(self, new_tile):
        self._tile = new_tile
        self._tile.color = self._tile.tile_type.color
        self._tile.__class__ = self.tile_type
    
