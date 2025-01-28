import sqlite3

from services.ExpenseService import ExpenseService
from services.IncomeService import IncomeService


class BudgetService:

    expense = None
    income = None

    def __init__(self, expense: ExpenseService, income: IncomeService):
        self.expense = expense
        self.income = income
        pass

    def budget_calculator(self):

        total_spending = self.expense.track_spending()

        total_income = self.income.track_income()

        return total_income - total_spending
