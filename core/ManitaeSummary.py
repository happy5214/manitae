from PyQt4 import QtGui, QtCore

from ui_ManitaeSummary import Ui_ManitaeSummary

class ManitaeSummary(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ManitaeSummary, self).__init__(parent)
        self.ui = Ui_ManitaeSummary()
        self.ui.setupUi(self)
