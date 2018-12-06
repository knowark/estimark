from estimark.application.models import Schedule


def test_schedule_instantiation():
    schedule = Schedule(name='Project XYZ Schedule')

    assert schedule.name == 'Project XYZ Schedule'
