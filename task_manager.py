import json


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = {
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        print("Task added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{index}. {task['title']} [{status}]")