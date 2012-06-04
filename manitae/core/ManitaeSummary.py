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

from PyQt4 import QtGui, QtCore

from ui_ManitaeSummary import Ui_ManitaeSummary

class ManitaeSummary(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ManitaeSummary, self).__init__(parent)
        self.ui = Ui_ManitaeSummary()
        self.ui.setupUi(self)
