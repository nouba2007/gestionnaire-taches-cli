import pytest
from task import Task


def test_create_task():
    task = Task(1, "Réviser", "Réviser Python", 1, "2026-12-01")

    assert task.id == 1
    assert task.title == "Réviser"
    assert task.status == "À faire"


def test_invalid_priority():
    with pytest.raises(ValueError):
        Task(1, "Réviser", "Python", 5, "2026-12-01")


def test_invalid_date():
    with pytest.raises(ValueError):
        Task(1, "Réviser", "Python", 1, "mauvaise-date")


def test_empty_title():
    with pytest.raises(ValueError):
        Task(1, "", "Python", 1, "2026-12-01")