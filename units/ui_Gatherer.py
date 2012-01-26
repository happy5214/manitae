# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gatherer.ui'
#
# Created: Thu Jan 26 15:28:05 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Gatherer(object):
    def setupUi(self, Gatherer):
        Gatherer.setObjectName(_fromUtf8("Gatherer"))
        Gatherer.resize(400, 300)
        Gatherer.setWindowTitle(QtGui.QApplication.translate("Gatherer", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_2 = QtGui.QGridLayout(Gatherer)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Gatherer)
        self.label.setText(QtGui.QApplication.translate("Gatherer", "Production level", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.prodLevelLineEdit = QtGui.QLineEdit(Gatherer)
        self.prodLevelLineEdit.setReadOnly(True)
        self.prodLevelLineEdit.setObjectName(_fromUtf8("prodLevelLineEdit"))
        self.horizontalLayout_2.addWidget(self.prodLevelLineEdit)
        self.label_3 = QtGui.QLabel(Gatherer)
        self.label_3.setText(QtGui.QApplication.translate("Gatherer", " /turn", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(Gatherer)
        self.label_2.setText(QtGui.QApplication.translate("Gatherer", "Employees", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.employeeLineEdit = QtGui.QLineEdit(Gatherer)
        self.employeeLineEdit.setReadOnly(True)
        self.employeeLineEdit.setObjectName(_fromUtf8("employeeLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.employeeLineEdit)
        self.label_4 = QtGui.QLabel(Gatherer)
        self.label_4.setText(QtGui.QApplication.translate("Gatherer", "Production On", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.prodOnCheckBox = QtGui.QCheckBox(Gatherer)
        self.prodOnCheckBox.setText(_fromUtf8(""))
        self.prodOnCheckBox.setObjectName(_fromUtf8("prodOnCheckBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.prodOnCheckBox)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)

        self.retranslateUi(Gatherer)
        QtCore.QMetaObject.connectSlotsByName(Gatherer)

    def retranslateUi(self, Gatherer):
        pass

