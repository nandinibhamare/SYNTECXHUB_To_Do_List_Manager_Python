import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter task name: ").strip()

    if task_name == "":
        print("Task name cannot be empty.")
        return

    tasks.append({
        "title": task_name,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    print("\n========== TASK LIST ==========")

    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['title']} [{status}]")

    input("\nPress Enter to return to menu...")


def mark_task_completed(tasks):
    if not tasks:
        print("No tasks available.")
        return

    view_tasks_without_pause(tasks)

    try:
        task_number = int(input("Enter task number to mark complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    view_tasks_without_pause(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Deleted: {deleted_task['title']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def view_tasks_without_pause(tasks):
    print("\n========== TASK LIST ==========")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")


def show_menu():
    print("\n========== TO-DO LIST MANAGER ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_task_completed(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using To-Do List Manager.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()