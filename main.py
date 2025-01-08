import sqlite3

sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()

with open('sql/create_table_expenses.sql', 'r') as sql:
    query = sql.read()

cursor.execute(query)


def add_expense_category(expense):
    query = ''' INSERT INTO Expenses (category)
    VALUES 
    (?);
    '''
    cursor.execute(query, (expense,))
    sqliteConnection.commit()


new_expense = input("Enter a new expense category: ")
add_expense_category(new_expense)

cursor.close()
sqliteConnection.close()
