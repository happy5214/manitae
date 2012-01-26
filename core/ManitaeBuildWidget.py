from PyQt4 import QtGui, QtCore

from ui_ManitaeBuildWidget import Ui_ManitaeBuildWidget

class ManitaeBuildWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ManitaeBuildWidget, self).__init__(parent)
        self.ui = Ui_ManitaeBuildWidget()
        self.ui.setupUi(self)
