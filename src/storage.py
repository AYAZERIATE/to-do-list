import json
def load_tasks():
    try:
        with open("data/tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("data/tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)