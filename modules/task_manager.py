import json
import os
from datetime import datetime

TASK_FILE = os.path.join("data", "tasks.json")


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    title = input("Task title: ").strip()
    priority = input("Priority (Low/Medium/High): ").capitalize()

    task = {
        "title": title,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task added.")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks.")
        return

    print("\n📋 TASK LIST")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['title']} ({task['priority']})")


def complete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        index = int(input("Task number to complete: ")) - 1
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("✅ Task marked complete.")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
