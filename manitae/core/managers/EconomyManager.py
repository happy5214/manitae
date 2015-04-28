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

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtProperty, pyqtSignal, pyqtSlot

from manitae.core.basetypes.Person import Person

from manitae.errors.OutOfMoneyError import OutOfMoneyError

class EconomyManager(QtCore.QObject): 
    
    def __init__(self, game):
        super(EconomyManager, self).__init__()
        self.game = game
        self._total_money = 250.0
        self.basic_tax_rate = 0.05
        self.unit_salaries = {}
        self.emp_salaries = {}
        self._construction_costs = 0.0
        
        self.game.main_window.ui.widget.ui.totalMoney.setText(self.display_money(self.total_money))
        self.game.main_window.ui.widget.ui.taxRevenue.setText(self.display_money(self.tax_revenue))
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
        money = "{:.2f}".format(amount)
#        if amount < 0:
#            return "<span style=\"color:#c00000\">" + money + "</span>"
        return money
    
    @pyqtProperty(dict)
    def income_taxes(self):
        temp = {}
        for k,v in self.emp_salaries.items():
            temp[k] = k.income_tax
        return temp
    
    @pyqtProperty(float)
    def total_money(self):
        return self._total_money
    
    @total_money.setter
    def total_money(self, value):
        self._total_money = value
        self.game.main_window.ui.widget.ui.totalMoney.setText(self.display_money(self._total_money))
    
    @pyqtProperty(float)
    def tax_revenue(self):
        taxes = self.income_taxes.values()
        return sum(taxes)
    
    @pyqtProperty(float)
    def total_revenue(self):
        return self.tax_revenue
    
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
        self.emp_salaries.update(unit.emp_to_salary)
        for emp in unit.employees:
            emp.employer_production_switched()
        
        self.game.main_window.ui.widget.ui.taxRevenue.setText(self.display_money(self.tax_revenue))
        self.game.main_window.ui.widget.ui.totalRevenue.setText(self.display_money(self.total_revenue))
        self.game.main_window.ui.widget.ui.workersSalary.setText(self.display_money(self.salaries))
        self.game.main_window.ui.widget.ui.totalExpenses.setText(self.display_money(self.total_expenses))
        self.game.main_window.ui.widget.ui.totalProfit.setText(self.display_money(self.total_profit))
    
    def on_turn_end(self, turn_number):
        change = self.total_profit
        self.total_money += change
        
        self.construction_costs = 0.0
        
        self.game.main_window.ui.widget.ui.taxRevenue.setText(self.display_money(self.tax_revenue))
        self.game.main_window.ui.widget.ui.totalRevenue.setText(self.display_money(self.total_revenue))
        self.game.main_window.ui.widget.ui.workersSalary.setText(self.display_money(self.salaries))
        self.game.main_window.ui.widget.ui.constructionCosts.setText(self.display_money(self.construction_costs))
        self.game.main_window.ui.widget.ui.totalExpenses.setText(self.display_money(self.total_expenses))
        self.game.main_window.ui.widget.ui.totalProfit.setText(self.display_money(self.total_profit))
    
