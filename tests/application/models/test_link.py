from estimark.application.models import Link


def test_link_instantiation():
    link = Link(id='L001', source='T001', target='T020')

    assert link.id == 'L001'
    assert link.source == 'T001'
    assert link.target == 'T020'
