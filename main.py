import sqlite3


def create_expense_table():
    with open('sql/create_table_expenses.sql', 'r') as sql:
        query = sql.read()

    cursor.execute(query)


def add_expense_category(expense):
    with open('sql/insert_expense_category.sql', 'r') as sql:
        query = sql.read()

    cursor.execute(query, (expense,))
    sqliteConnection.commit()


sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()

create_expense_table()
new_expense = input("Enter a new expense category: ")
add_expense_category(new_expense)

cursor.close()
sqliteConnection.close()
