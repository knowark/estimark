from estimark.application.models import Effort


def test_effort_instantiation():
    effort = Effort(kind='time', units='hours', amount=4)

    assert effort.kind == 'time'
    assert effort.units == 'hours'
    assert effort.amount == 4
