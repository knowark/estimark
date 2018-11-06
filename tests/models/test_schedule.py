from estimark.application.models import Schedule


def test_schedule_instantiation():
    schedule = Schedule(id='S001', name='Project XYZ Schedule')

    assert schedule.id == 'S001'
    assert schedule.name == 'Project XYZ Schedule'
