from database import init_db
from user import User
from task import Task

def main():
    init_db()
    print("Welcome to Productivity App\n")

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            user.register()

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = User.login(username, password)

            if user_id:
                while True:
                    print("1. Add Task")
                    print("2. Show Tasks")
                    print("3. Delete Task")
                    print("4. Logout")
                    action = input("Choose action: ")

                    if action == "1":
                        title = input("Enter task title: ")
                        task = Task(user_id, title)
                        task.add_task()

                    elif action == "2":
                        Task.show_tasks(user_id)

                    elif action == "3":
                        task_id = int(input("Enter task ID to delete: "))
                        Task.delete_task(task_id)

                    elif action == "4":
                        print("Logged out\n")
                        break
                    else:
                        print("Invalid option\n")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option\n")

if __name__ == "__main__":
    main()
