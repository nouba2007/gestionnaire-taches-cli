from pathlib import Path

from task import Task
from sauvegarde import save_tasks, load_tasks


def test_save_and_load_tasks(tmp_path: Path):
    filename = tmp_path / "data.json"

    original_tasks = [
        Task(1, "Python", "Apprendre Python", 1, "2026-12-01"),
        Task(2, "Maths", "Faire les exercices", 2, "2026-12-02")
    ]

    save_tasks(original_tasks, filename)
    loaded_tasks = load_tasks(filename)

    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].title == "Python"
    assert loaded_tasks[1].title == "Maths"
