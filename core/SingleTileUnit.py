from PyQt4.QtCore import pyqtProperty

from Unit import Unit
from maps.MapTile import MapTile

class SingleTileUnit(Unit):
    
    tile_type = MapTile
    
    @pyqtProperty(MapTile)
    def tile(self):
        return self._tile
    
    @tile.setter
    def tile(self, new_tile):
        self._tile = new_tile
        self._tile.__class__ = self.tile_type
    
