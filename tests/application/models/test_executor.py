from estimark.application.models import Executor


def test_executor_instantiation():
    executor = Executor(id='jdacevedo', name='José Daniel Acevedo')

    assert executor.id == 'jdacevedo'
    assert executor.name == 'José Daniel Acevedo'
