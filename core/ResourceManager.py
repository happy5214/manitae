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
    
