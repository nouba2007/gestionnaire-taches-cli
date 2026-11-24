from task import Task


def get_sort_key(task: Task, criterion: str):
    """Détermine la valeur utilisée pour comparer les tâches."""

    if criterion == "priority":
        return task.priority

    if criterion == "due_date":
        return task.due_date

    if criterion == "status":
        status_order = {
            "À faire": 1,
            "En cours": 2,
            "Terminée": 3
        }
        return status_order[task.status]

    raise ValueError("Critère de tri inconnu.")


def merge(left: list[Task], right: list[Task], criterion: str) -> list[Task]:
    """Fusionne deux listes déjà triées."""

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if (
            get_sort_key(left[i], criterion)
            <= get_sort_key(right[j], criterion)
        ):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(tasks: list[Task], criterion: str) -> list[Task]:
    """Trie les tâches avec l'algorithme Merge Sort."""

    if len(tasks) <= 1:
        return tasks.copy()

    middle = len(tasks) // 2

    left = merge_sort(tasks[:middle], criterion)
    right = merge_sort(tasks[middle:], criterion)

    return merge(left, right, criterion)


def sort_tasks(tasks: list[Task], criterion: str) -> list[Task]:
    """Trie les tâches selon un critère donné."""

    if criterion not in ("priority", "due_date", "status"):
        raise ValueError("Critère de tri invalide.")

    return merge_sort(tasks, criterion)