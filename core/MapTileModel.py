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

from PyQt4.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt

class MapTileModel(QAbstractTableModel):
    def __init__(self, map_data):
        super(MapTileModel, self).__init__()
        self.map_data = map_data
        self.ColorRole = Qt.UserRole + 1
        self.TileRole = Qt.UserRole + 2
        roles = {self.ColorRole: "color", self.TileRole: "tile"}
        self.setRoleNames(roles)
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.map_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.map_data[0])
    
    def data(self, index, role):
        if not(index.isValid()):
            return QVariant()
        if (role == self.ColorRole):
            return self.map_data[index.row()][index.column()].color
        elif (role == self.TileRole):
            return self.map_data[index.row()][index.column()].tile
        else:
            return QVariant()
    
