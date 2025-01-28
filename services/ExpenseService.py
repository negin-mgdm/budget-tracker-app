import sqlite3


class ExpenseService:

    cursor = None
    sqliteConnection = None

    def __init__(self, cursor: sqlite3.Cursor, sqliteConnection: sqlite3.Connection):
        self.cursor = cursor
        self.sqliteConnection = sqliteConnection

    def create_expense_table(self):
        with open("sql/create_table_expenses.sql", "r") as sql:
            query = sql.read()

        self.cursor.execute(query)

    def add_expense_category(self, expense):
        with open("sql/insert_expense_category.sql", "r") as sql:
            query = sql.read()

        self.cursor.execute(query, (expense,))
        self.sqliteConnection.commit()

    def update_expense_amount(self, category, amount):
        with open("sql/update_expense_amount.sql", "r") as sql:
            query = sql.read()

            self.cursor.execute(query, (amount, category))
            self.sqliteConnection.commit()

    def delete_expense_category(self, id):
        with open("sql/delete_expense_category.sql", "r") as sql:
            query = sql.read()

            self.cursor.execute(query, id)
            self.sqliteConnection.commit()

    def track_spending(self):
        with open("sql/fetch_spending.sql", "r") as sql:
            query = sql.read()

            self.cursor.execute(query)
            amounts = self.cursor.fetchall()

            spendings = 0
            for amount in amounts:
                spendings += amount[0]
            return spendings

    def view_expenses_by_category(self, category):
        with open("sql/fetch_expenses_by_category.sql", "r") as sql:
            query = sql.read()

            self.cursor.execute(query, (category,))
            row = self.cursor.fetchone()

            return row[0]
