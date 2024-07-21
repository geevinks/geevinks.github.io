import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('telegram_bot.db')
cursor = conn.cursor()

# Create a table to store users and their money variable
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        money INTEGER DEFAULT 0
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
