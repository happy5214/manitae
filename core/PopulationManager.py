import pkgutil

from PyQt4 import QtCore

from ManitaeGame import *
import people

class PopulationManager(QtCore.QObject):
    
    def __init__(self, game):
        super(PopulationManager, self).__init__()
        self.game = game
        self.setup_population_types()
        self.setup_basic_population()
        self.employed = 0
        
        self.game.main_window.ui.widget.ui.totalPopulation.setText(str(len(self.population)))
        self.game.main_window.ui.widget.ui.workingPopulation.setText(str(self.employed))
    
    def setup_population_types(self):
        """Sets up the resource_types list."""
        self.population_types = []
        for x in pkgutil.walk_packages(['people']):
            if not(x[1].startswith('ui_')):
                self.population_types.append(x[1])
        for x in self.population_types:
            __import__("people." + x)
    
    def setup_basic_population(self):
        self.population = []
        for x in range(5):
            self.population.append(people.Citizen.Citizen())
        
    def allocate_employee_to_unit(self, unit, number):
        emp_count = 0
        for person in self.population:
            if (person.TYPE in unit.employee_types) and not(person.employer):
                unit.employees.append(person)
                person.employer = unit
                emp_count += 1
            if (emp_count == number):
                break
        self.employed += emp_count
        self.game.main_window.ui.widget.ui.workingPopulation.setText(str(self.employed))
