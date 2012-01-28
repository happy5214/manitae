from core.Person import Person 

class Citizen(Person):
    
    TYPE = "Citizen"
    level = 0
    
    def __init__(self):
        super(Citizen, self).__init__()
    
