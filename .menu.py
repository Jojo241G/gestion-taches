
print("bonjour a tous")

"""from task_manager import add_task, modify_task, delete_task, list_tasks, tasks
from json_handler import  save_to_file, load_from_file


def menu():
    filename = "tasks.json"
    loaded = load_from_file(filename)
    tasks.extend(loaded)

    while True:
        print("\n=== MENU ===")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Modifier une tâche")
        print("4. Supprimer une tâche")
        print("5. Sauvegarder et quitter")
        choix = input("Choix : ")

        if choix == "1":
            list_tasks()
        elif choix == "2":
            t = input("Nouvelle tâche : ")
            add_task(t)
        elif choix == "3":
            list_tasks()
            i = int(input("Numéro de tâche à modifier : ")) - 1
            t = input("Nouvelle description : ")
            modify_task(i, t)
        elif choix == "4":
            list_tasks()
            i = int(input("Numéro de tâche à supprimer : ")) - 1
            delete_task(i)
        elif choix == "5":
            save_to_file(filename, tasks)
            print("Tâches sauvegardées.")
            break
        else:
            print("Choix invalide.")"""
