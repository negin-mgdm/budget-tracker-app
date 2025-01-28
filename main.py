import sqlite3

from services.ExpenseService import ExpenseService
from services.IncomeService import IncomeService


class BudgetService:

    def budget_calculator(self):
        expense = ExpenseService()
        total_spending = expense.track_spending()

        income = IncomeService()
        total_income = income.track_income()

        return total_income - total_spending


def setup_tables():
    expense = ExpenseService(cursor, sqliteConnection)
    expense.create_expense_table()

    income = IncomeService(cursor, sqliteConnection)
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

    expense = ExpenseService(cursor, sqliteConnection)
    income = IncomeService(cursor, sqliteConnection)
    budget = BudgetService()

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
                calculated_budget = budget.budget_calculator()
                print(f"{message}{calculated_budget}")

            case 0:
                break


sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()

setup_tables()

main_menu()

cursor.close()
sqliteConnection.close()
