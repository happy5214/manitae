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

from manitae.core.basetypes.Unit import Unit

class Producer(Unit):
    
    employee_fired = QtCore.pyqtSignal('QString')
    employee_hired = QtCore.pyqtSignal('QString')
    needs_employee = QtCore.pyqtSignal(Unit, int)
    production_switched = QtCore.pyqtSignal()
    salary_changed = QtCore.pyqtSignal(float)
    
    def __init__(self):
        super(Producer, self).__init__()
    
    def ready_for_allocation(self):
        pass
