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


def add_income_category(income, category):
    with open("sql/insert_income_category.sql", "r") as sql:
        query = sql.read()

    cursor.execute(query, (income, category))
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


def create_income_table():
    with open("sql/create_income_table.sql", "r") as sql:
        query = sql.read()

    cursor.execute(query)


def delete_income_by_category(category):
    with open("sql/delete_income_category.sql", "r") as sql:
        query = sql.read()

        cursor.execute(query, (category,))
        sqliteConnection.commit()


def track_spending():
    with open("sql/fetch_spending.sql", "r") as sql:
        query = sql.read()

        cursor.execute(query)
        amounts = cursor.fetchall()

        spendings = 0
        for amount in amounts:
            spendings += amount[0]
        return spendings


def track_income():
    with open("sql/fetch_income.sql", "r") as sql:
        query = sql.read()

        cursor.execute(query)
        amounts = cursor.fetchall()

        income = 0
        for amount in amounts:
            income += amount[0]
        return income


def view_income_by_category(category):
    with open("sql/fetch_income_by_category.sql", "r") as sql:
        query = sql.read()

        cursor.execute(query, (category,))
        row = cursor.fetchone()

        return row[0]


def setup_tables():
    create_expense_table()
    create_income_table()


def main_menu():

    menu = '''1. Add a new expense category 
2. Update a category amount
3. Delete an expense category
4. Add income category and amount
5. Delete an income category
6. Fetch all spendings
7. Fetch income
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

        elif option == 3:
            id = input(
                "Please enter the category id you wish to remove from the 'Expenses' table: ")
            delete_expense_category(id)

        elif option == 4:
            income_amount = input("Enter amount for the income: ")
            income_category = input("Enter an income category: ")
            add_income_category(income_amount, income_category)

        elif option == 5:
            category = input(
                "Please enter the category you wish to remove from the 'Income' table: ")
            delete_income_by_category(category)

        elif option == 6:
            all_expenses = track_spending()
            print(f"Your total spending is: {all_expenses}")

        elif option == 7:
            all_income = track_income()
            print(f"Your total income is: {all_income}")

        elif option == 0:
            break


sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()

category = input("Enter the category you wish to see the income for: ")
print(view_income_by_category(category))

setup_tables()

main_menu()

cursor.close()
sqliteConnection.close()
