from estimark.application.models import Effort


def test_effort_instantiation():
    effort = Effort(id='TIME001', kind='time', units='hours', amount=4)

    assert effort.id == 'TIME001'
    assert effort.kind == 'time'
    assert effort.units == 'hours'
    assert effort.amount == 4
