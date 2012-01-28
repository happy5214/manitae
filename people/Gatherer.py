from Citizen import *

class Gatherer(Citizen):
    
    TYPE = "Gatherer"
    level = 1
    
    def __init__(self):
        super(Gatherer, self).__init__()
