import json
from app.task import Task



def save_tasks(tasks, filename="tasks.json"):
    data = [task.to_dict() for task in tasks]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        tasks = [Task.from_dict(dictionary) for dictionary in data]
        return tasks
    except FileNotFoundError:
        return []