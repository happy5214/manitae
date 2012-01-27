from PyQt4 import QtCore

class ManitaeLogger(QtCore.QObject):
    send_entry = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(ManitaeLogger, self).__init__()
    
    def append_notice(self, notice):
        temp_string = "<p style=\"margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; white-space:pre-wrap\">" + notice + "</p><br/>\n";
        self.send_entry.emit(temp_string)
    
    def append_warning(self, warning):
        tempString = "<p style=\"margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; white-space:pre-wrap; color:#c00000\">" + warning + "</p><br/>\n";
        self.send_entry.emit(tempString);
    
