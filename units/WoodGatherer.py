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

from PyQt4.QtCore import pyqtSignal, pyqtProperty, pyqtSlot
from PyQt4.QtGui import QWidget, QStringListModel, QMessageBox

from core.LevelOnePrimitiveProducer import *
from ui_PrimitiveProducer import Ui_PrimitiveProducer

class WoodGatherer(LevelOnePrimitiveProducer):
    
    UNIT = "Wood Gatherer"
    level = 1
    
    employee_types = ['Citizen', 'Wood Gatherer']
    employee_efficiency = {'Citizen': 2, 'Wood Gatherer': 3}
    employee_salary = {'Citizen': 7.50, 'Wood Gatherer': 10.00}
    employee_max = 1
    
    construction_cost = 20
    
    def __init__(self):
        super(WoodGatherer, self).__init__()
    
    def on_turn_end(self, turn_number):
        if self.production_on:
            self.change_primitive_resource.emit("Wood", self.production_rate)
            self.employees[0].gain_experience("Wood Gatherer", 1)
    
