from estimark.application.models import Schedule


def test_schedule_instantiation():
    schedule = Schedule(id='PR001', name='Project XYZ Schedule')

    assert schedule.id == 'PR001'
    assert schedule.name == 'Project XYZ Schedule'
