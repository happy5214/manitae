# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hunter.ui'
#
# Created: Thu Jan 26 13:22:08 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Hunter(object):
    def setupUi(self, Hunter):
        Hunter.setObjectName(_fromUtf8("Hunter"))
        Hunter.resize(400, 300)
        Hunter.setWindowTitle(QtGui.QApplication.translate("Hunter", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_2 = QtGui.QGridLayout(Hunter)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Hunter)
        self.label.setText(QtGui.QApplication.translate("Hunter", "Production level", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.prodLevelLineEdit = QtGui.QLineEdit(Hunter)
        self.prodLevelLineEdit.setReadOnly(True)
        self.prodLevelLineEdit.setObjectName(_fromUtf8("prodLevelLineEdit"))
        self.horizontalLayout_2.addWidget(self.prodLevelLineEdit)
        self.label_3 = QtGui.QLabel(Hunter)
        self.label_3.setText(QtGui.QApplication.translate("Hunter", " /turn", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(Hunter)
        self.label_2.setText(QtGui.QApplication.translate("Hunter", "Employees", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.employeeLineEdit = QtGui.QLineEdit(Hunter)
        self.employeeLineEdit.setReadOnly(True)
        self.employeeLineEdit.setObjectName(_fromUtf8("employeeLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.employeeLineEdit)
        self.label_4 = QtGui.QLabel(Hunter)
        self.label_4.setText(QtGui.QApplication.translate("Hunter", "Production On", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.prodOnCheckBox = QtGui.QCheckBox(Hunter)
        self.prodOnCheckBox.setText(_fromUtf8(""))
        self.prodOnCheckBox.setObjectName(_fromUtf8("prodOnCheckBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.prodOnCheckBox)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)

        self.retranslateUi(Hunter)
        QtCore.QMetaObject.connectSlotsByName(Hunter)

    def retranslateUi(self, Hunter):
        pass

