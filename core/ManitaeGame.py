from PyQt4 import QtGui, QtCore

from ManitaeMainWindow import *
from ManitaeLogger import *
from ResourceManager import *
from TurnManager import *
from UnitManager import *

class ManitaeGame(QtCore.QObject):
    def __init__(self, main_window):
        super(ManitaeGame, self).__init__()
        self.main_window = main_window
        
        self.logger = ManitaeLogger()
        self.logger.send_entry.connect(self.add_log_entry)
        self.logger.append_notice("New game started.")
        
        self.resource_manager = ResourceManager(self)
        self.turn_manager = TurnManager(self)
        self.unit_manager = UnitManager(self)
        
        self.extra_tabs = []
        
        self.main_window.ui.widget.ui.resourceComboBox.setModel(self.resource_manager.resource_type_model)
        self.main_window.ui.widget.ui.resourceComboBox.activated[str].connect(self.update_resource_widget)
        self.main_window.ui.widget_2.ui.comboBox.setModel(self.unit_manager.unit_type_model)
        self.main_window.ui.widget_2.ui.pushButton.clicked.connect(self.build)
        
        self.resource_manager.resource_changed.connect(self.update_resource_widget_after_turn)
        
        self.main_window.ui.widget.ui.resourceLineEdit.setText('0')
    
    def add_log_entry(self, log_entry):
        temp_cursor = self.main_window.ui.widget.ui.noticeLog.textCursor()
        temp_cursor.movePosition(QtGui.QTextCursor.End)
        self.main_window.ui.widget.ui.noticeLog.setTextCursor(temp_cursor)
        self.main_window.ui.widget.ui.noticeLog.insertHtml(log_entry)
    
    def add_tab(self, tab, name):
        self.main_window.ui.tabWidget.addTab(tab, name)
        self.extra_tabs.append(tab)
    
    def build(self):
        unit = self.main_window.ui.widget_2.ui.comboBox.currentText()
        self.unit_manager.build(unit)
    
    def end_turn(self):
        self.turn_manager.end_turn()
    
    def restart_game(self):
        for x in self.extra_tabs:
            self.main_window.ui.tabWidget.removeTab(self.main_window.ui.tabWidget.indexOf(x))
        del self.extra_tabs
        del self.resource_manager
        del self.turn_manager
        del self.unit_manager
        #
        
        self.turn_manager = TurnManager(self)
        self.logger.append_notice("New game started.")
        
        self.resource_manager = ResourceManager(self)
        self.unit_manager = UnitManager(self)
        
        self.extra_tabs = []
        
        self.main_window.ui.widget.ui.resourceComboBox.setModel(self.resource_manager.resource_type_model)
        self.main_window.ui.widget_2.ui.comboBox.setModel(self.unit_manager.unit_type_model)
        
        self.resource_manager.resource_changed.connect(self.update_resource_widget_after_turn)
        
        self.main_window.ui.widget.ui.resourceLineEdit.setText('0')
    
    def update_resource_widget(self, resource):
        res_amount = self.resource_manager.resources[str(resource)]
        self.main_window.ui.widget.ui.resourceLineEdit.setText(str(res_amount))
    
    def update_resource_widget_after_turn(self, resource_changed):
        resource = self.main_window.ui.widget.ui.resourceComboBox.currentText()
        if resource == resource_changed:
            res_amount = self.resource_manager.resources[str(resource)]
            self.main_window.ui.widget.ui.resourceLineEdit.setText(str(res_amount))
