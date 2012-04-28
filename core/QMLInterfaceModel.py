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

from PyQt4.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt

class QMLInterfaceModel(QAbstractListModel):
    def __init__(self, model):
        super(QMLInterfaceModel, self).__init__()
        self.model = model
        self.ColorRole = Qt.UserRole + 1
        self.TileRole = Qt.UserRole + 2
        self.CoordsRole = Qt.UserRole + 3
        roles = {self.ColorRole: "color", self.TileRole: "tile", self.CoordsRole: "coords"}
        self.setRoleNames(roles)
    
    def rowCount(self, parent=QModelIndex()):
        return self.model.rowCount() * self.model.columnCount()
    
    def data(self, index, role):
        column, row = self.index_to_coords(index.row())
        if role == self.CoordsRole:
            return (row, column)
        new_index = self.model.index(row, column)
        return self.model.data(new_index, role)
    
    def index_to_coords(self, row):
        column = row // self.model.rowCount()
        coord_row = row % self.model.rowCount()
        return (column, coord_row)
    
    def coords_to_index(self, coords):
        return coords[0] * self.model.rowCount() + coords[1]
    
