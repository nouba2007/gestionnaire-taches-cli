from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: str
    due_date: str
    statut: str = "À faire"