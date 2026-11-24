import json
from pathlib import Path
from dataclasses import asdict

from task import Task


DATA_FILE = Path(__file__).parent / "data" / "data.json"


def save_tasks(tasks: list[Task], filename: Path = DATA_FILE) -> None:
    """Enregistre les tâches dans un fichier JSON."""

    filename.parent.mkdir(parents=True, exist_ok=True)

    data = [asdict(task) for task in tasks]

    with filename.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_tasks(filename: Path = DATA_FILE) -> list[Task]:
    """Charge les tâches depuis un fichier JSON."""

    if not filename.exists():
        return []

    with filename.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Le fichier JSON doit contenir une liste.")

    tasks = []

    for item in data:
        tasks.append(Task(**item))

    return tasks
