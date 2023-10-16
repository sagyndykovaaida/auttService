import sqlite3
import bcrypt

# Connect to the SQLite database
sqlite_conn = sqlite3.connect('../authRegisterService/users.db')
sqlite_cursor = sqlite_conn.cursor()

# Insert data into the SQLite database
username = 'example_user'
password = 'example_password'
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
sqlite_cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                     (username, hashed_password))
sqlite_conn.commit()
sqlite_conn.close()
