import sqlite3

# Connect to the database
conn = sqlite3.connect('telegram_bot.db')
c = conn.cursor()

# Create a table for users
c.execute('''CREATE TABLE users
             (user_id INTEGER PRIMARY KEY, money INTEGER)''')

# Commit changes and close the connection
conn.commit()
conn.close()