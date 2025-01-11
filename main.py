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


def delete_expense_category(id):
    with open("sql/delete_expense_category.sql", "r") as sql:
        query = sql.read()

        cursor.execute(query, id)
        sqliteConnection.commit()


def main_menu():

    menu = '''1. Add a new expense category 
2. Update a category amount
0. Exit
Please enter your option from the above menu: '''

    while True:
        option = int(input(menu))

        if option == 1:
            new_expense = input("Enter a new expense category: ")
            add_expense_category(new_expense)

        elif option == 2:
            category = input(
                "Insert the category you wish to update the amount: ")
            amount = input(
                f"Insert the updated expense amount for the '{category}' category: ")
            update_expense_amount(category, amount)

        elif option == 0:
            break


sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()

create_expense_table()
main_menu()

cursor.close()
sqliteConnection.close()
