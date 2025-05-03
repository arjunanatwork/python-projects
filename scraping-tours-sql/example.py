import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)

new_rows = [('New Year', 'Happy New Year!', '2020-01-01')]
cursor.executemany('INSERT INTO events VALUES (?, ?, ?)', new_rows)
connection.commit()