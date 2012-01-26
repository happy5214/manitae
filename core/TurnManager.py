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
