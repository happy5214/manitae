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

class MapTile(QtCore.QObject):
    """Base class for map tiles."""
    
    buildable = True
    """Whether buildings can be built on this tile."""
    tile = ""
    """Tile image, specified as a relative path from this directory, i.e. \"./tile_images/<base type>/<type>/<image>\""""
    tile_type = None
    """Original class of the tile, used as a backup in case of the destruction of the resident unit."""
    unit = None
    """Resident unit."""
    
    def __init__(self, tile=None):
        super(MapTile, self).__init__()
        if not(self.tile) and tile:
            self.tile = tile
            self.buildable = False
    
MapTile.tile_type = MapTile
