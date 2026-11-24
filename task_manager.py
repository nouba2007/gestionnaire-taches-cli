from task import Task

class TaskManager:
    """Gère l'ensemble des tâches."""

    def __init__(self) -> None:
        self.tasks: dict[int, Task] = {}
        self.next_id: int = 1

    def add_task(
        self,
        title: str,
        description: str,
        priority: str,
        due_date: str,
    ) -> Task:
        """Ajoute une nouvelle tâche à la liste des tâches."""
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
        )
        self.tasks[self.next_id] = task
        self.next_id += 1        
        return task

    def list_tasks(self) -> list[Task]:
        """Retourne la liste des tâches triées par identifiant."""
        return [self.tasks[task_id] for task_id in sorted(self.tasks)]

    def get_task(self, task_id: int) -> Task | None:
        """Récupère une tâche par son identifiant."""
        return self.tasks.get(task_id)
    
    def remove_task(self, task_id: int) -> bool:
        """Supprime une tâche si elle existe."""
        return self.tasks.pop(task_id, None) is not None

    def mark_task_done(self, task_id: int) -> Task | None:
        """Marque une tâche comme terminée."""
        task = self.tasks.get(task_id)
        if task is None:
            return None
        task.statut = "Terminée"
        return task