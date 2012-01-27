class NoMoreWorkersError(Exception):
    def __init__(self, unit_type):
        self.unit_type = unit_type
    
    def __str__(self):
        return "Could not build {0}: no more available workers. Try destroying some other units or wait for more workers to become available.".format(self.unit_type)
