from task_manager import TaskManager
from recherche import search_tasks
from tri import sort_tasks
from sauvegarde import save_tasks, load_tasks
from utils import read_integer, read_priority, read_date, display_task


def display_menu():
    """Affiche le menu principal."""

    print("\n========== GESTIONNAIRE DE TÂCHES ==========")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Modifier une tâche")
    print("4. Supprimer une tâche")
    print("5. Marquer une tâche comme terminée")
    print("6. Rechercher une tâche")
    print("7. Trier les tâches")
    print("8. Sauvegarder les tâches")
    print("9. Quitter")
    print("============================================")


def add_task(manager):
    """Permet d'ajouter une tâche."""

    print("\n--- AJOUT D'UNE TÂCHE ---")

    title = input("Titre : ").strip()
    description = input("Description : ").strip()
    priority = read_priority()
    due_date = read_date()

    try:
        task = manager.add_task(
            title,
            description,
            priority,
            due_date
        )

        print(f"Tâche ajoutée avec succès. ID : {task.id}")

    except ValueError as error:
        print(f"Erreur : {error}")


def show_tasks(manager):
    """Affiche toutes les tâches."""

    tasks = manager.list_tasks()

    if not tasks:
        print("Aucune tâche enregistrée.")
        return

    print("\n--- LISTE DES TÂCHES ---")

    for task in tasks:
        display_task(task)


def modify_task(manager):
    """Permet de modifier une tâche."""

    task_id = read_integer("Identifiant de la tâche : ")
    task = manager.get_task(task_id)

    if task is None:
        print("Tâche introuvable.")
        return

    print("Laisse vide les champs que tu ne souhaites pas modifier.")

    title = input("Nouveau titre : ").strip()
    description = input("Nouvelle description : ").strip()

    updates = {}

    if title:
        updates["title"] = title

    if description:
        updates["description"] = description

    change_priority = input("Modifier la priorité ? (o/n) : ").lower()

    if change_priority == "o":
        updates["priority"] = read_priority()

    change_date = input("Modifier la date ? (o/n) : ").lower()

    if change_date == "o":
        updates["due_date"] = read_date()

    if manager.update_task(task_id, **updates):
        print("Tâche modifiée avec succès.")
    else:
        print("Modification impossible ou aucune modification effectuée.")


def delete_task(manager):
    """Supprime une tâche."""

    task_id = read_integer("Identifiant de la tâche à supprimer : ")

    if manager.delete_task(task_id):
        print("Tâche supprimée avec succès.")
    else:
        print("Tâche introuvable.")


def complete_task(manager):
    """Marque une tâche comme terminée."""

    task_id = read_integer("Identifiant de la tâche : ")

    if manager.mark_task_done(task_id):
        print("Tâche marquée comme terminée.")
    else:
        print("Tâche introuvable.")


def search_task(manager):
    """Recherche une tâche par mot-clé."""

    keyword = input("Mot-clé à rechercher : ").strip()

    results = search_tasks(manager.list_tasks(), keyword)

    if not results:
        print("Aucun résultat trouvé.")
        return

    print("\n--- RÉSULTATS DE LA RECHERCHE ---")

    for task in results:
        display_task(task)


def sort_task(manager):
    """Trie les tâches selon un critère."""

    print("\n1. Trier par priorité")
    print("2. Trier par date limite")
    print("3. Trier par statut")

    choice = read_integer("Votre choix : ")

    criteria = {
        1: "priority",
        2: "due_date",
        3: "status"
    }

    criterion = criteria.get(choice)

    if criterion is None:
        print("Choix invalide.")
        return

    tasks = sort_tasks(manager.list_tasks(), criterion)

    print("\n--- TÂCHES TRIÉES ---")

    for task in tasks:
        display_task(task)


def main():
    """Fonction principale de l'application."""

    manager = TaskManager()

    try:
        manager.load_tasks(load_tasks())
        print("Données précédentes chargées.")
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f"Impossible de charger les données : {error}")
        print("Le programme démarre avec une liste vide.")

    while True:
        display_menu()

        choice = read_integer("Votre choix : ")

        if choice == 1:
            add_task(manager)

        elif choice == 2:
            show_tasks(manager)

        elif choice == 3:
            modify_task(manager)

        elif choice == 4:
            delete_task(manager)

        elif choice == 5:
            complete_task(manager)

        elif choice == 6:
            search_task(manager)

        elif choice == 7:
            sort_task(manager)

        elif choice == 8:
            try:
                save_tasks(manager.list_tasks())
                print("Sauvegarde effectuée avec succès.")
            except OSError as error:
                print(f"Erreur de sauvegarde : {error}")

        elif choice == 9:
            try:
                save_tasks(manager.list_tasks())
                print("Données sauvegardées. À bientôt !")
            except OSError as error:
                print(f"Erreur de sauvegarde : {error}")

            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
