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

import pkgutil

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal, pyqtProperty, pyqtSlot

from ManitaeGame import *
from Person import *
import people

class PopulationManager(QtCore.QObject):
    
    level_ups_ready = pyqtSignal()
    
    def __init__(self, game):
        super(PopulationManager, self).__init__()
        self.game = game
        self.population = []
        self.population_types = []
        self.setup_population_types()
        self.setup_basic_population()
        self.employed = 0
        Person.id_inc = 1
        
        self.game.main_window.ui.widget.ui.totalPopulation.setText(str(len(self.population)))
        self.game.main_window.ui.widget.ui.workingPopulation.setText(str(self.employed))
    
    def __del__(self):
        for x in self.population:
            self.game.main_window.ui.peopleTabWidget.removeTab(self.game.main_window.ui.peopleTabWidget.indexOf(x.widget))
    
    def setup_population_types(self):
        """Sets up the population_types list."""
        for x in pkgutil.walk_packages(['people']):
            if not(x[1].startswith('ui_')):
                self.population_types.append(x[1])
        for x in self.population_types:
            __import__("people." + x)
    
    def setup_basic_population(self):
        for x in range(5):
            pop = people.Citizen.Citizen()
            self.population.append(pop)
            self.game.main_window.ui.peopleTabWidget.addTab(pop.widget, str(pop))
            self.game.turn_manager.turn_ended.connect(pop.on_turn_end)
            pop.name_changed_sig.connect(self.person_name_changed)
            pop.send_notice.connect(self.game.logger.append_notice)
            pop.send_warning.connect(self.game.logger.append_warning)
            self.level_ups_ready.connect(pop.refresh_level_up_type_model)
        self.level_one_people()
        
    def allocate_employee_to_unit(self, unit, number):
        emp_count = 0
        self.population.sort(key=Person.key, reverse=True)
        for person in self.population:
            if (person.TYPE in unit.employee_types) and not(person.employer):
                unit.employees.append(person)
                person.employer = unit
                emp_count += 1
            if (emp_count == number):
                break
        self.employed += emp_count
        self.update_eligible_workers(unit)
        for u in self.game.unit_manager.units:
            self.update_eligible_workers(u)
        self.game.main_window.ui.widget.ui.workingPopulation.setText(str(self.employed))
    
    @pyqtProperty(dict)
    def str_to_person(self):
        temp = {}
        for p in self.population:
            temp[str(p)] = p
        return temp
    
    def employee_fired(self, amount):
        self.employed -= amount
        for x in self.game.unit_manager.units:
            self.update_eligible_workers(x)
        self.game.main_window.ui.widget.ui.workingPopulation.setText(str(self.employed))
    
    def employee_hired(self, amount):
        self.employed += amount
        for x in self.game.unit_manager.units:
            self.update_eligible_workers(x)
        self.game.main_window.ui.widget.ui.workingPopulation.setText(str(self.employed))
    
    def update_eligible_workers(self, unit):
        elig_pop_list = []
        elig_pop_str_list = []
        for person in self.population:
            if (person.TYPE in unit.employee_types) and not(person.employer):
                elig_pop_list.append(person)
        for person in elig_pop_list:
            elig_pop_str_list.append(str(person))
        unit.hirable_model.setStringList(elig_pop_str_list)
    
    def level_one_people(self):
        elig_pop_type_list = []
        for person_type in self.population_types:
            if (eval("people.{0}.{0}.level".format(person_type)) == 1):
                elig_pop_type_list.append(eval("people.{0}.{0}.TYPE".format(person_type)))
        people.Citizen.Citizen.level_up_types = elig_pop_type_list
        self.level_ups_ready.emit()
    
    def person_name_changed(self):
        for x in self.game.unit_manager.units:
            self.update_eligible_workers(x)
            x.employee_model.setStringList(x.employee_string_list)
        self.game.main_window.ui.peopleTabWidget.setTabText(self.game.main_window.ui.peopleTabWidget.indexOf(self.sender().widget), str(self.sender()))
    
