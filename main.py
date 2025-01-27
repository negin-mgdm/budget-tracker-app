import sqlite3


class ExpenseService:

    def create_expense_table(self):
        with open("sql/create_table_expenses.sql", "r") as sql:
            query = sql.read()

        cursor.execute(query)

    def add_expense_category(self, expense):
        with open("sql/insert_expense_category.sql", "r") as sql:
            query = sql.read()

        cursor.execute(query, (expense,))
        sqliteConnection.commit()

    def update_expense_amount(self, category, amount):
        with open("sql/update_expense_amount.sql", "r") as sql:
            query = sql.read()

            cursor.execute(query, (amount, category))
            sqliteConnection.commit()

    def delete_expense_category(self, id):
        with open("sql/delete_expense_category.sql", "r") as sql:
            query = sql.read()

            cursor.execute(query, id)
            sqliteConnection.commit()

    def track_spending(self):
        with open("sql/fetch_spending.sql", "r") as sql:
            query = sql.read()

            cursor.execute(query)
            amounts = cursor.fetchall()

            spendings = 0
            for amount in amounts:
                spendings += amount[0]
            return spendings

    def view_expenses_by_category(self, category):
        with open("sql/fetch_expenses_by_category.sql", "r") as sql:
            query = sql.read()

            cursor.execute(query, (category,))
            row = cursor.fetchone()

            return row[0]


class IncomeService:

    def create_income_table(self):
        with open("sql/create_income_table.sql", "r") as sql:
            query = sql.read()

        cursor.execute(query)

    def add_income_category(self, income, category):
        with open("sql/insert_income_category.sql", "r") as sql:
            query = sql.read()

        cursor.execute(query, (income, category))
        sqliteConnection.commit()

    def track_income(self):
        with open("sql/fetch_income.sql", "r") as sql:
            query = sql.read()

            cursor.execute(query)
            amounts = cursor.fetchall()

            income = 0
            for amount in amounts:
                income += amount[0]
            return income

    def view_income_by_category(self, category):
        with open("sql/fetch_income_by_category.sql", "r") as sql:
            query = sql.read()

            cursor.execute(query, (category,))
            row = cursor.fetchone()

            return row[0]

    def delete_income_by_category(self, category):
        with open("sql/delete_income_category.sql", "r") as sql:
            query = sql.read()

            cursor.execute(query, (category,))
            sqliteConnection.commit()


def budget_calculator():
    expense = ExpenseService()
    total_spending = expense.track_spending()

    income = IncomeService()
    total_income = income.track_income()
    return total_income - total_spending


def setup_tables():
    expense = ExpenseService()
    expense.create_expense_table()

    income = IncomeService()
    income.create_income_table()


def main_menu():

    menu = '''1. Add a new expense category 
2. Update a category amount
3. Delete an expense category
4. Add income category and amount
5. Delete an income category
6. Fetch all spendings
7. Fetch income
8. View income by category
9. View expenses by category
10. Budget
0. Exit
Please enter your option from the above menu: '''

    expense = ExpenseService()
    income = IncomeService()

    while True:
        option = int(input(menu))

        match (option):
            case 1:
                new_expense = input("Enter a new expense category: ")
                expense.add_expense_category(new_expense)

            case 2:
                category = input(
                    "Insert the category you wish to update the amount: ")
                amount = input(
                    f"Insert the updated expense amount for the '{category}' category: ")
                expense.update_expense_amount(category, amount)

            case 3:
                id = input(
                    "Please enter the category id you wish to remove from the 'Expenses' table: ")
                expense.delete_expense_category(id)

            case 4:
                income_amount = input("Enter amount for the income: ")
                income_category = input("Enter an income category: ")
                income.add_income_category(income_amount, income_category)

            case 5:
                category = input(
                    "Please enter the category you wish to remove from the 'Income' table: ")
                income.delete_income_by_category(category)

            case 6:
                all_expenses = expense.track_spending()
                print(f"Your total spending is: {all_expenses}")

            case 7:
                all_income = income.track_income()
                print(f"Your total income is: {all_income}")

            case 8:
                category = input(
                    "Enter the category you wish to see the income for: ")
                income_by_category = income.view_income_by_category(category)
                print(
                    f"The income for '{category}' category is {income_by_category}.")

            case 9:
                category = input(
                    "Enter the category you wish to see the expenses for: ")
                expenses_by_category = expense.view_expenses_by_category(
                    category)
                print(
                    f"The income for '{category}' category is {expenses_by_category}.")

            case 10:
                message = "Your budget is: "
                budget = budget_calculator()
                print(f"{message}{budget}")

            case 0:
                break


sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()

setup_tables()

main_menu()

cursor.close()
sqliteConnection.close()
