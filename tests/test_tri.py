from task import Task
from tri import sort_tasks


def create_tasks():
    return [
        Task(1, "Java", "POO", 3, "2026-12-03"),
        Task(2, "Python", "Algorithmique", 1, "2026-12-01"),
        Task(3, "Maths", "Analyse", 2, "2026-12-02")
    ]


def test_sort_by_priority():
    tasks = sort_tasks(create_tasks(), "priority")

    assert [task.priority for task in tasks] == [1, 2, 3]


def test_sort_by_date():
    tasks = sort_tasks(create_tasks(), "due_date")

    assert [task.due_date for task in tasks] == [
        "2026-12-01",
        "2026-12-02",
        "2026-12-03"
    ]


def test_sort_by_status():
    tasks = [
        Task(1, "A", "Test", 1, "2026-12-01", "Terminée"),
        Task(2, "B", "Test", 2, "2026-12-02", "À faire"),
        Task(3, "C", "Test", 3, "2026-12-03", "En cours")
    ]

    result = sort_tasks(tasks, "status")

    assert [task.status for task in result] == [
        "À faire",
        "En cours",
        "Terminée"
    ]
