from PyQt4 import QtCore

class Person(QtCore.QObject):
    
    TYPE = "Person"
    level = -1
    id_inc = 1
    
    def __init__(self):
        super(Person, self).__init__()
        self.employer = None
        self.id = Person.id_inc
        Person.id_inc += 1
    
    def __str__(self):
        return "{0} (Level {1}): id {2}".format(self.TYPE, self.level, str(self.id))
    
    def key(self):
        return self.level
