import json

def save_to_file(filename, tasks):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def load_from_file(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
