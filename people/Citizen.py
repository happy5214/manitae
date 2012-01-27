from core.Person import Person 

class Citizen(Person):
    
    TYPE = "Citizen"
    
    def __init__(self):
        super(Citizen, self).__init__()
    
    