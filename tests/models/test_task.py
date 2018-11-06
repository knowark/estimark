from estimark.application.models import Task


def test_task_instantiation():
    task = Task(id='T001', name='Deploy Application Server')

    assert task.id == 'T001'
    assert task.name == 'Deploy Application Server'
