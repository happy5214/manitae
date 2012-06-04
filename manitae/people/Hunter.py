#   Copyright (C) 2012 Alexander Jones
#
#   This file is part of Manitae.
#
#   Manitae is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Manitae is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Manitae.  If not, see <http://www.gnu.org/licenses/>.

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
