from task import Task
from recherche import search_tasks, contains_manual


def test_manual_search():
    assert contains_manual("Programmation Python", "python")


def test_search_tasks():
    tasks = [
        Task(1, "Python", "Programmation", 1, "2026-12-01"),
        Task(2, "Mathématiques", "Analyse", 2, "2026-12-02")
    ]

    results = search_tasks(tasks, "python")

    assert len(results) == 1
    assert results[0].id == 1