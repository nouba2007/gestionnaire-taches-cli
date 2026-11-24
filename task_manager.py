from dataclasses import replace
from task import Task


class TaskManager:
    """Gère les tâches à l'aide d'un dictionnaire."""

    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add_task(
        self,
        title: str,
        description: str,
        priority: int,
        due_date: str
    ) -> Task:
        """Ajoute une nouvelle tâche."""

        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            priority=priority,
            due_date=due_date
        )

        self._tasks[task.id] = task
        self._next_id += 1

        return task

    def list_tasks(self) -> list[Task]:
        """Retourne la liste des tâches."""

        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Task | None:
        """Recherche une tâche par son identifiant."""

        return self._tasks.get(task_id)

    def update_task(self, task_id: int, **updates) -> bool:
        """Modifie les informations d'une tâche."""

        task = self.get_task(task_id)

        if task is None:
            return False

        allowed_fields = {
            "title",
            "description",
            "priority",
            "due_date",
            "status"
        }

        if not updates or any(
            field not in allowed_fields for field in updates
        ):
            return False

        try:
            updated_task = replace(task, **updates)
        except (TypeError, ValueError):
            return False

        self._tasks[task_id] = updated_task
        return True

    def delete_task(self, task_id: int) -> bool:
        """Supprime une tâche."""

        return self._tasks.pop(task_id, None) is not None

    def mark_task_done(self, task_id: int) -> bool:
        """Marque une tâche comme terminée."""

        return self.update_task(task_id, status="Terminée")

    def load_tasks(self, tasks: list[Task]) -> None:
        """Charge une liste de tâches dans le gestionnaire."""

        self._tasks = {task.id: task for task in tasks}

        if self._tasks:
            self._next_id = max(self._tasks) + 1
        else:
            self._next_id = 1