import sqlite3

class Task:
    def __init__(self, user_id, title):
        self.user_id = user_id
        self.title = title

    def add_task(self):
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (user_id, title, done) VALUES (?, ?, ?)",
            (self.user_id, self.title, 0)
        )
        conn.commit()
        conn.close()
        print(f"Task '{self.title}' added successfully\n")

    @staticmethod
    def show_tasks(user_id):
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, done FROM tasks WHERE user_id=?",
            (user_id,)
        )
        tasks = cursor.fetchall()
        conn.close()

        if not tasks:
            print("No tasks found.\n")
        else:
            print("Your tasks:")
            for t in tasks:
                status = "Done" if t[2] else "Not Done"
                print(f"ID: {t[0]}, Title: {t[1]}, Status: {status}")
            print()

    @staticmethod
    def delete_task(task_id):
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        conn.close()
        print(f"Task ID {task_id} deleted successfully\n")
