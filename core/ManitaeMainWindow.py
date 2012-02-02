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

from ManitaeSummary import *
from ManitaeGame import *

from ui_ManitaeMainWindow import Ui_ManitaeMainWindow

class ManitaeMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ManitaeMainWindow, self).__init__(parent)
        self.ui = Ui_ManitaeMainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew_Game.triggered.connect(self.start_new_game)
        self.game = None
    
    def start_new_game(self):
        if self.game == None:
            self.game = ManitaeGame(self)
            self.ui.actionEnd_Turn.triggered.connect(self.game.end_turn)
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("There is already a game in progress.")
            msgBox.setInformativeText("Are you sure you want to start a new one?")
            msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            msgBox.setDefaultButton(QtGui.QMessageBox.No)
            ret = msgBox.exec_()
            if ret == QtGui.QMessageBox.Yes:
                self.game.restart_game()
            else:
                pass
        
