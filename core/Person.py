from PyQt4 import QtCore

class Person(QtCore.QObject):

    def __init__(self):
        super(Person, self).__init__()
        self.employer = None
        