import sqlite3


def create_expense_table():
    with open("sql/create_table_expenses.sql", "r") as sql:
        query = sql.read()

    cursor.execute(query)


def add_expense_category(expense):
    with open("sql/insert_expense_category.sql", "r") as sql:
        query = sql.read()

    cursor.execute(query, (expense,))
    sqliteConnection.commit()


def update_expense_amount(category, amount):
    with open("sql/update_expense_amount.sql", "r") as sql:
        query = sql.read()

        cursor.execute(query, (amount, category))
        sqliteConnection.commit()


sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()

create_expense_table()
new_expense = input("Enter a new expense category: ")
add_expense_category(new_expense)

category = input("Insert the category you wish to update the amount: ")
amount = input(
    f"Insert the updated expense amount for the '{category}' category: ")
update_expense_amount(category, amount)

cursor.close()
sqliteConnection.close()
