import sqlite3

sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()

query = '''CREATE TABLE IF NOT EXISTS Expenses (
    expense_id INTEGER PRIMARY KEY,
    category TEXT NOT NULL
    );'''

cursor.execute(query)
