# task_manager.py
# INTENTIONALLY WRONG CODE — DEBUG IT 🙂

import json
from datetime import datetime

TASK_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            file = open(TASK_FILE, "r")
            data = json.load(file)
            return data
        except:
            return {}

    def save_tasks(self):
        with open(TASK_FILE, "w") as f:
            json.dump(self.tasks, f)

    def add_task(self, title, due_date):
        task_id = len(self.tasks)
        self.tasks[task_id] = {
            "title": title,
            "due": datetime.strptime(due_date, "%Y/%m/%d"),
            "done": "False"
        }
        print("Task added")

    def complete_task(self, task_id):
        self.tasks[task_id]["done"] = True
        print("Completed!")

    def list_tasks(self):
        for t in self.tasks:
            task = self.tasks[t]
            print(f"{t}. {task['title']} - Due: {task['due']} - Done: {task['done']}")

def main():
    manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == 1:
            title = input("Title: ")
            due = input("Due date (YYYY-MM-DD): ")
            manager.add_task(title, due)

        elif choice == 2:
            tid = input("Task id: ")
            manager.complete_task(tid)

        elif choice == 3:
            manager.list_tasks()

        elif choice == 4:
            manager.save_tasks()
            break

        else:
            print("Invalid option")

main()