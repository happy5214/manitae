from Citizen import *

class WoodGatherer(Citizen):
    
    TYPE = "Wood Gatherer"
    level = 1
    
    def __init__(self):
        super(WoodGatherer, self).__init__()
