from task_manager import TaskManager


def create_manager():
    manager = TaskManager()
    manager.add_task("Python", "Apprendre Python", 1, "2026-12-01")
    return manager


def test_add_task():
    manager = create_manager()
    assert len(manager.list_tasks()) == 1


def test_get_task():
    manager = create_manager()
    assert manager.get_task(1).title == "Python"


def test_delete_task():
    manager = create_manager()
    assert manager.delete_task(1) is True
    assert len(manager.list_tasks()) == 0


def test_mark_task_done():
    manager = create_manager()
    assert manager.mark_task_done(1) is True
    assert manager.get_task(1).status == "Terminée"


def test_update_task():
    manager = create_manager()
    assert manager.update_task(1, title="Java")
    assert manager.get_task(1).title == "Java"
