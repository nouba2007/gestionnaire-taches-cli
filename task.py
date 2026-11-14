from dataclasse imprt dataclass
@dataclass
class task:
    id: int
    title: str
    description : str
    priority : str
    due_date :str
    statut : str = "A farie"