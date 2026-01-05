import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (self.username, self.password)
        )
        conn.commit()
        conn.close()
        print(f"User '{self.username}' registered successfully\n")

    @staticmethod
    def login(username, password):
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM users WHERE username=? AND password=?",
            (username, password)
        )
        result = cursor.fetchone()
        conn.close()

        if result:
            print(f"User '{username}' logged in successfully\n")
            return result[0]
        else:
            print("Login failed. Check username/password\n")
            return None
