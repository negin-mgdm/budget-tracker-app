import sqlite3

sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()

query = '''CREATE TABLE IF NOT EXISTS Expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL
    );'''

cursor.execute(query)


def add_expense_category():
    query = ''' INSERT INTO Expenses (category)
    VALUES 
    ('utility'),
    ('rent');
    '''
    cursor.execute(query)
    sqliteConnection.commit()


add_expense_category()

cursor.close()
sqliteConnection.close()
