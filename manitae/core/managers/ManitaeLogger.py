#   Copyright (C) 2012 Alexander Jones
#
#   This file is part of Manitae.
#
#   Manitae is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Manitae is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Manitae.  If not, see <http://www.gnu.org/licenses/>.

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
    
