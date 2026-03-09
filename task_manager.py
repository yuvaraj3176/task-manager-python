import json


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):

        task = {
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def list_tasks(self):

        if not self.tasks:
            print("No tasks available.")
            return

        for index, task in enumerate(self.tasks, start=1):

            status = "✔" if task["completed"] else "✘"
            print(f"{index}. {task['title']} [{status}]")

    # MEMBER 3 FEATURE
    # Delete Task

    def delete_task(self, task_number):

        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number")
            return

        removed_task = self.tasks.pop(task_number - 1)
        self.save_tasks()

        print(f"Deleted task: {removed_task['title']}")

    # MEMBER 3 FEATURE
    # Save tasks to JSON file

    def save_tasks(self):

        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    # MEMBER 3 FEATURE
    # Load tasks from JSON

    def load_tasks(self):

        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

        except FileNotFoundError:
            self.tasks = []