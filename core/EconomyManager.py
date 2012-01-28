from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtProperty, pyqtSignal, pyqtSlot

from ManitaeGame import *
from Person import *

from OutOfMoneyError import *

class EconomyManager(QtCore.QObject):
    
    def __init__(self, game):
        super(EconomyManager, self).__init__()
        self.game = game
        self._total_money = 250.0
        self._total_revenue = 0.0
        self.unit_salaries = {}
        self._construction_costs = 0.0
        
        self.game.main_window.ui.widget.ui.totalMoney.setText(self.display_money(self.total_money))
        self.game.main_window.ui.widget.ui.totalRevenue.setText(self.display_money(self.total_revenue))
        self.game.main_window.ui.widget.ui.workersSalary.setText(self.display_money(self.salaries))
        self.game.main_window.ui.widget.ui.constructionCosts.setText(self.display_money(self.construction_costs))
        self.game.main_window.ui.widget.ui.totalExpenses.setText(self.display_money(self.total_expenses))
        self.game.main_window.ui.widget.ui.totalProfit.setText(self.display_money(self.total_profit))
        
    
    def build(self, unit):
        cost = unit.construction_cost
        costs_so_far = self.total_expenses
        new_cost = cost + costs_so_far
        if new_cost > self.total_money:
            raise OutOfMoneyError("Could not build {0}".format(unit.UNIT))
        else:
            self.construction_costs += cost
            self.unit_salaries[unit] = 0.0
            unit.salary_changed.connect(self.unit_salary_changed)
    
    def display_money(self, amount):
        return "{:.2f}".format(amount)
    
    @pyqtProperty(float)
    def total_money(self):
        return self._total_money
    
    @total_money.setter
    def total_money(self, value):
        self._total_money = value
        self.game.main_window.ui.widget.ui.totalMoney.setText(self.display_money(self._total_money))
    
    @pyqtProperty(float)
    def total_revenue(self):
        return self._total_revenue
    
    @pyqtProperty(float)
    def total_expenses(self):
        return self.salaries + self._construction_costs
    
    @pyqtProperty(float)
    def salaries(self):
        unit_salaries = self.unit_salaries.values()
        return sum(unit_salaries)
    
    @pyqtProperty(float)
    def construction_costs(self):
        return self._construction_costs
    
    @construction_costs.setter
    def construction_costs(self, value):
        self._construction_costs = value
        self.game.main_window.ui.widget.ui.constructionCosts.setText(self.display_money(self._construction_costs))
        self.game.main_window.ui.widget.ui.totalExpenses.setText(self.display_money(self.total_expenses))
        self.game.main_window.ui.widget.ui.totalProfit.setText(self.display_money(self.total_profit))
    
    @pyqtProperty(float)
    def total_profit(self):
        return self.total_revenue - self.total_expenses
    
    @pyqtSlot(float)
    def unit_salary_changed(self, new_salary):
        unit = self.sender()
        self.unit_salaries[unit] = new_salary
        self.game.main_window.ui.widget.ui.workersSalary.setText(self.display_money(self.salaries))
        self.game.main_window.ui.widget.ui.totalExpenses.setText(self.display_money(self.total_expenses))
        self.game.main_window.ui.widget.ui.totalProfit.setText(self.display_money(self.total_profit))
    
    def on_turn_end(self, turn_number):
        change = self.total_profit
        self.total_money += change
        
        self.construction_costs = 0.0
        
        self.game.main_window.ui.widget.ui.workersSalary.setText(self.display_money(self.salaries))
        self.game.main_window.ui.widget.ui.constructionCosts.setText(self.display_money(self.construction_costs))
        self.game.main_window.ui.widget.ui.totalExpenses.setText(self.display_money(self.total_expenses))
        self.game.main_window.ui.widget.ui.totalProfit.setText(self.display_money(self.total_profit))
    
