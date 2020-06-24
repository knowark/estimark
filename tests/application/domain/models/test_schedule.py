from estimark.application.domain.models import Schedule


def test_schedule_instantiation():
    schedule = Schedule(id='PR001', name='Project XYZ Schedule')

    assert schedule.id == 'PR001'
    assert schedule.name == 'Project XYZ Schedule'
    assert schedule.state == ''
