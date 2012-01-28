from Citizen import *

class Hunter(Citizen):
    
    TYPE = "Hunter"
    level = 1
    
    def __init__(self):
        super(Hunter, self).__init__()
