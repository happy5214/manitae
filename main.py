#!/usr/bin/env python

import sys

from PyQt4 import QtGui, QtCore

from core.ManitaeMainWindow import ManitaeMainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mmw = ManitaeMainWindow()
    mmw.showMaximized()
    sys.exit(app.exec_())
