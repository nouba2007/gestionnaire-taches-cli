from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Représente une tâche dans le gestionnaire."""

    id: int
    title: str
    description: str
    priority: int
    due_date: str
    status: str = "À faire"

    def __post_init__(self):
        """Vérifie la validité des informations de la tâche."""

        if not self.title.strip():
            raise ValueError("Le titre ne peut pas être vide.")

        if self.priority not in (1, 2, 3):
            raise ValueError("La priorité doit être 1, 2 ou 3.")

        try:
            date.fromisoformat(self.due_date)
        except ValueError:
            raise ValueError("La date doit respecter le format AAAA-MM-JJ.")

        if self.status not in ("À faire", "En cours", "Terminée"):
            raise ValueError("Statut invalide.")