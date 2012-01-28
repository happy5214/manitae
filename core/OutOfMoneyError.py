class OutOfMoneyError(Exception):
    def __init__(self, action):
        self.action = action
    
    def __str__(self):
        return "{0}: out of available money. Wait for more money to become available.".format(self.action)
