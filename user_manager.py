import sqlite3
import bcrypt

class UserManager:
    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.conn = sqlite3.connect('../authRegisterService/users.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def register_user(self, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                            (username, hashed_password))
        self.conn.commit()
        return True

    def authenticate_user(self, username, password):
        self.cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = self.cursor.fetchone()

        if result:
            stored_password = result[0]
            return bcrypt.checkpw(password.encode('utf-8'), stored_password)
        return False

    def close_connection(self):
        self.conn.close()
