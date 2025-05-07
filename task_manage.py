tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def modify_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task

def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]

def list_tasks():
    for i, t in enumerate(tasks):
        print(f"{i + 1}. {t['task']} - {'Terminée' if t['done'] else 'En cours'}")
