from task import Task


def contains_manual(text: str, keyword: str) -> bool:
    """Recherche manuellement un mot dans une chaîne."""

    text = text.lower()
    keyword = keyword.lower()

    if keyword == "":
        return True

    if len(keyword) > len(text):
        return False

    for i in range(len(text) - len(keyword) + 1):
        found = True

        for j in range(len(keyword)):
            if text[i + j] != keyword[j]:
                found = False
                break

        if found:
            return True

    return False


def search_tasks(tasks: list[Task], keyword: str) -> list[Task]:
    """Recherche une tâche dans son titre ou sa description."""

    results = []

    for task in tasks:
        if (
            contains_manual(task.title, keyword)
            or contains_manual(task.description, keyword)
        ):
            results.append(task)

    return results