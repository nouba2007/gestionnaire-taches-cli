from datetime import date


def read_integer(message: str) -> int:
    """Demande un nombre entier à l'utilisateur."""

    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


def read_priority() -> int:
    """Demande une priorité valide."""

    while True:
        priority = read_integer(
            "Priorité (1=Haute, 2=Moyenne, 3=Basse) : "
        )

        if priority in (1, 2, 3):
            return priority

        print("La priorité doit être 1, 2 ou 3.")


def read_date() -> str:
    """Demande une date valide au format AAAA-MM-JJ."""

    while True:
        value = input("Date limite (AAAA-MM-JJ) : ").strip()

        try:
            date.fromisoformat(value)
            return value
        except ValueError:
            print("Date invalide. Exemple : 2026-12-31.")


def display_task(task) -> None:
    """Affiche les informations d'une tâche."""

    priorities = {
        1: "Haute",
        2: "Moyenne",
        3: "Basse"
    }

    print("-" * 50)
    print(f"ID          : {task.id}")
    print(f"Titre       : {task.title}")
    print(f"Description : {task.description}")
    print(f"Priorité    : {priorities[task.priority]}")
    print(f"Date limite : {task.due_date}")
    print(f"Statut      : {task.status}")
    print("-" * 50)