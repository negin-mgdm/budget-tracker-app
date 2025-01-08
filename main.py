import sqlite3

sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()

query = '''CREATE TABLE IF NOT EXISTS Expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL
    );'''

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
