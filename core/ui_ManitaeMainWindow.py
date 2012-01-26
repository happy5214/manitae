# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManitaeMainWindow.ui'
#
# Created: Wed Jan 25 18:26:24 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManitaeMainWindow(object):
    def setupUi(self, ManitaeMainWindow):
        ManitaeMainWindow.setObjectName(_fromUtf8("ManitaeMainWindow"))
        ManitaeMainWindow.resize(856, 568)
        ManitaeMainWindow.setWindowTitle(QtGui.QApplication.translate("ManitaeMainWindow", "Manitae", None, QtGui.QApplication.UnicodeUTF8))
        self.centralWidget = QtGui.QWidget(ManitaeMainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = ManitaeSummary(self.tab)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widget_2 = ManitaeBuildWidget(self.tab_2)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        ManitaeMainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ManitaeMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 856, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuGame = QtGui.QMenu(self.menuBar)
        self.menuGame.setTitle(QtGui.QApplication.translate("ManitaeMainWindow", "Game", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGame.setObjectName(_fromUtf8("menuGame"))
        self.menuStats = QtGui.QMenu(self.menuBar)
        self.menuStats.setTitle(QtGui.QApplication.translate("ManitaeMainWindow", "Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.menuStats.setObjectName(_fromUtf8("menuStats"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setTitle(QtGui.QApplication.translate("ManitaeMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        ManitaeMainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ManitaeMainWindow)
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setFloatable(False)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        ManitaeMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ManitaeMainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ManitaeMainWindow.setStatusBar(self.statusBar)
        self.actionNew_Game = QtGui.QAction(ManitaeMainWindow)
        self.actionNew_Game.setText(QtGui.QApplication.translate("ManitaeMainWindow", "New Game", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Game.setShortcut(QtGui.QApplication.translate("ManitaeMainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Game.setObjectName(_fromUtf8("actionNew_Game"))
        self.actionEnd_Turn = QtGui.QAction(ManitaeMainWindow)
        self.actionEnd_Turn.setText(QtGui.QApplication.translate("ManitaeMainWindow", "End Turn", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnd_Turn.setShortcut(QtGui.QApplication.translate("ManitaeMainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnd_Turn.setObjectName(_fromUtf8("actionEnd_Turn"))
        self.actionExit = QtGui.QAction(ManitaeMainWindow)
        self.actionExit.setText(QtGui.QApplication.translate("ManitaeMainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("ManitaeMainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPopulation = QtGui.QAction(ManitaeMainWindow)
        self.actionPopulation.setText(QtGui.QApplication.translate("ManitaeMainWindow", "Population", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPopulation.setShortcut(QtGui.QApplication.translate("ManitaeMainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPopulation.setObjectName(_fromUtf8("actionPopulation"))
        self.actionEconomy = QtGui.QAction(ManitaeMainWindow)
        self.actionEconomy.setText(QtGui.QApplication.translate("ManitaeMainWindow", "Economy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEconomy.setShortcut(QtGui.QApplication.translate("ManitaeMainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEconomy.setObjectName(_fromUtf8("actionEconomy"))
        self.actionResources = QtGui.QAction(ManitaeMainWindow)
        self.actionResources.setText(QtGui.QApplication.translate("ManitaeMainWindow", "Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResources.setShortcut(QtGui.QApplication.translate("ManitaeMainWindow", "Ctrl+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResources.setObjectName(_fromUtf8("actionResources"))
        self.actionResearch = QtGui.QAction(ManitaeMainWindow)
        self.actionResearch.setText(QtGui.QApplication.translate("ManitaeMainWindow", "Research", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResearch.setShortcut(QtGui.QApplication.translate("ManitaeMainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResearch.setObjectName(_fromUtf8("actionResearch"))
        self.actionHelp = QtGui.QAction(ManitaeMainWindow)
        self.actionHelp.setText(QtGui.QApplication.translate("ManitaeMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setShortcut(QtGui.QApplication.translate("ManitaeMainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuGame.addAction(self.actionNew_Game)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.actionEnd_Turn)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.actionExit)
        self.menuStats.addAction(self.actionPopulation)
        self.menuStats.addAction(self.actionEconomy)
        self.menuStats.addAction(self.actionResearch)
        self.menuStats.addAction(self.actionResources)
        self.menuHelp.addAction(self.actionHelp)
        self.menuBar.addAction(self.menuGame.menuAction())
        self.menuBar.addAction(self.menuStats.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(ManitaeMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), ManitaeMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(ManitaeMainWindow)

    def retranslateUi(self, ManitaeMainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("ManitaeMainWindow", "Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ManitaeMainWindow", "Build", None, QtGui.QApplication.UnicodeUTF8))

from ManitaeSummary import ManitaeSummary
from ManitaeBuildWidget import ManitaeBuildWidget
