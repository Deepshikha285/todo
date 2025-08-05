# todo.py

import os

# File to store tasks persistently
TASK_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from file into a list."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [task.strip() for task in file.readlines() if task.strip()]


def save_tasks(tasks):
    """Save the list of tasks to the file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(task, tasks):
    """Add a task to the list and save."""
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("📭 Your to-do list is empty.")
        return
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def remove_task(index, tasks):
    """Remove a task by its index and save."""
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task removed: {removed}")
    except IndexError:
        print("❌ Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                add_task(new_task, tasks)
            else:
                print("⚠️ Task cannot be empty.")
        elif choice == "3":
            view_tasks(tasks)
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index, tasks)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            print("👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("❌ Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
