from Citizen import *

class Hunter(Citizen):
    
    TYPE = "Hunter"
    level = 1
    level_up_types = []
    upgrade_exp_reqs = {'Hunter': 10}
    
    def __init__(self):
        super(Hunter, self).__init__()
    
    @staticmethod
    def upgrade_to(person):
        conditions_met = False
        for k,v in Hunter.upgrade_exp_reqs.items():
            try:
                if person.experience[k] >= v:
                    conditions_met = True
                    break
            except KeyError:
                pass
        if (conditions_met):
            person.__class__ = Hunter
            
            person.level_up_type_model.setStringList(Hunter.level_up_types)
            person.ui.typeLineEdit.setText(person.TYPE)
            person.ui.levelLineEdit.setText(str(person.level))
            person.ui.netWorthLineEdit.setText(person.display_money(person._net_worth))
            person.ui.salaryLineEdit.setText(person.display_money(person.salary))
            person.ui.taxesLineEdit.setText(person.display_money(person.income_tax))
            person.ui.netLineEdit.setText(person.display_money(person.net))
            
            return (True, '')
        else:
            return (False, 'Conditions not met.')
