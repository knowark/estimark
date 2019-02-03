from estimark.application.models import Role


def test_role_instantiation():
    role = Role(id='R1', name='Project Manager')

    assert role.id == 'R1'
    assert role.name == 'Project Manager'
