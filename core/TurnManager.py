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

from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot

from ManitaeGame import *

class TurnManager(QObject):
    turn_ended = pyqtSignal(int)
    
    def __init__(self, game):
        super(TurnManager, self).__init__()
        self.turn_number = 1
        self.game = game
        self.turn_ended.connect(self.display_turn_notice)
    
    def end_turn(self):
        self.turn_ended.emit(self.turn_number)
        self.turn_number += 1
    
    @pyqtSlot(int)
    def display_turn_notice(self, turn_number):
        temp = "Turn {0} has ended.".format(turn_number)
        self.game.logger.append_notice(temp)
