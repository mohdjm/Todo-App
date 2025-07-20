# todo-list-cli/main.py

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{idx + 1}. [{status}] {task['name']}")

def add_task(tasks):
    name = input("Enter task name: ")
    tasks.append({"name": name, "done": False})
    print("Task added.")
show_menu()
