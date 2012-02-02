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

import pkgutil

from PyQt4 import QtCore, QtGui

from ManitaeGame import *

class ResourceManager(QtCore.QObject):
    resource_changed = QtCore.pyqtSignal('QString')
    def __init__(self, game):
        super(ResourceManager, self).__init__()
        self.game = game
        self.setup_resource_types()
        self.resources = dict.fromkeys(self.resource_types, 0)
        self.resource_type_model = QtGui.QStringListModel(self.resource_types)
    
    def setup_resource_types(self):
        """Sets up the resource_types list."""
        self.resource_types = []
        for x in pkgutil.walk_packages(['resources']):
            if not(x[1].startswith('ui_')):
                self.resource_types.append(x[1])
    
    def update_primitive_resource(self, resource, change):
        resource = str(resource)
        self.resources[resource] += change
        self.game.logger.append_notice("{0} {1} added.".format(change, resource))
        self.resource_changed.emit(resource)
    
