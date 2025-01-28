import sqlite3


class IncomeService:

    cursor = None
    sqliteConnection = None

    def __init__(self, cursor: sqlite3.Cursor, sqliteConnection: sqlite3.Connection):
        self.cursor = cursor
        self.sqliteConnection = sqliteConnection
        pass

    def create_income_table(self):
        with open("sql/create_income_table.sql", "r") as sql:
            query = sql.read()

        self.cursor.execute(query)

    def add_income_category(self, income, category):
        with open("sql/insert_income_category.sql", "r") as sql:
            query = sql.read()

        self.cursor.execute(query, (income, category))
        self.sqliteConnection.commit()

    def track_income(self):
        with open("sql/fetch_income.sql", "r") as sql:
            query = sql.read()

            self.cursor.execute(query)
            amounts = self.cursor.fetchall()

            income = 0
            for amount in amounts:
                income += amount[0]
            return income

    def view_income_by_category(self, category):
        with open("sql/fetch_income_by_category.sql", "r") as sql:
            query = sql.read()

            self.cursor.execute(query, (category,))
            row = self.cursor.fetchone()

            return row[0]

    def delete_income_by_category(self, category):
        with open("sql/delete_income_category.sql", "r") as sql:
            query = sql.read()

            self.cursor.execute(query, (category,))
            self.sqliteConnection.commit()
