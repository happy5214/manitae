# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManitaeBuildWidget.ui'
#
# Created: Wed Jan 25 18:25:31 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManitaeBuildWidget(object):
    def setupUi(self, ManitaeBuildWidget):
        ManitaeBuildWidget.setObjectName(_fromUtf8("ManitaeBuildWidget"))
        ManitaeBuildWidget.resize(400, 300)
        ManitaeBuildWidget.setWindowTitle(QtGui.QApplication.translate("ManitaeBuildWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(ManitaeBuildWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox = QtGui.QComboBox(ManitaeBuildWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton = QtGui.QPushButton(ManitaeBuildWidget)
        self.pushButton.setText(QtGui.QApplication.translate("ManitaeBuildWidget", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(ManitaeBuildWidget)
        QtCore.QMetaObject.connectSlotsByName(ManitaeBuildWidget)

    def retranslateUi(self, ManitaeBuildWidget):
        pass

