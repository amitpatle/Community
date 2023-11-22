import sqlite3

# Connect to an SQLite database (if it doesn't exist, a new database will be created)
conn = sqlite3.connect('example.db')

# Create a cursor object using which you can interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Insert data into the table
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Bob', 25))

# Commit changes to the database
conn.commit()

# Retrieve data from the table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
