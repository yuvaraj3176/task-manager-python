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
    def mark_task_complete(self, task_number):
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number.")
            return

        self.tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")        