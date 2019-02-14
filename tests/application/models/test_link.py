from estimark.application.models import Link


def test_link_instantiation():
    link = Link(id='L001', predecessor_id='T001', successor_id='T020')

    assert link.id == 'L001'
    assert link.predecessor_id == 'T001'
    assert link.successor_id == 'T020'
