import sqlite3

from services.ExpenseService import ExpenseService
from services.IncomeService import IncomeService


class BudgetService:

    cursor = None
    sqliteConnection = None

    def __init__(self, cursor: sqlite3.Cursor, sqliteConnection: sqlite3.Connection):
        self.cursor = cursor
        self.sqliteConnection = sqliteConnection
        pass

    def budget_calculator(self):
        expense = ExpenseService(self.cursor, self.sqliteConnection)
        total_spending = expense.track_spending()

        income = IncomeService(self.cursor, self.sqliteConnection)
        total_income = income.track_income()

        return total_income - total_spending
