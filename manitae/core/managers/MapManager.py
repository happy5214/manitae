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

from PyQt4 import QtCore, QtGui

from manitae.maps.models.MapTileModel import MapTileModel
from manitae.maps.models.QMLInterfaceModel import QMLInterfaceModel

class MapManager(QtCore.QObject):
    def __init__(self, game):
        super(MapManager, self).__init__()
        self.game = game
        self.map_data = self.game.scenario.setup_map()
        self.map_model = MapTileModel(self.map_data)
        self.model = QMLInterfaceModel(self.map_model)
        
        self.game.main_window.ui.mapView.rootContext().setContextProperty("map_model", self.model)
        self.game.main_window.ui.mapView.setSource(QtCore.QUrl("./manitae/maps/Map.qml"))
        
        self.qml_root = self.game.main_window.ui.mapView.rootObject()
        self.qml_root.resize(self.model.model.columnCount(), self.model.model.rowCount())
        self.qml_root.mapClicked.connect(self.update_current_tile)
        
        self.game.main_window.ui.goToTabPushButton.clicked.connect(self.go_to_tab)
    
    def update_current_tile(self, tile_index):
        self.current_tile_coords = self.model.index_to_coords(tile_index)
        self.current_tile = self.map_data[self.current_tile_coords[1]][self.current_tile_coords[0]]
        self.update_data(self.current_tile_coords, self.current_tile)
    
    def update_data(self, coords, tile):
        self.game.main_window.ui.buildPushButton.setEnabled(tile.buildable)
        self.game.main_window.ui.positionLineEdit.setText(str(coords))
        if tile.unit:
            self.game.main_window.ui.tileOccupantLineEdit.setText(str(tile.unit))
            self.game.main_window.ui.goToTabPushButton.setEnabled(True)
        else:
            self.game.main_window.ui.tileOccupantLineEdit.setText("")
            self.game.main_window.ui.goToTabPushButton.setEnabled(False)
        
    def go_to_tab(self):
        tab = self.current_tile.unit.widget
        self.game.main_window.ui.tabWidget.setCurrentWidget(tab)
    
