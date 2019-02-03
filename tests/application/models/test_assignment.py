from estimark.application.models import Assignment


def test_assignment_creation() -> None:
    id_ = "1"
    executor_id = "1"
    role_id = "1"

    assignment = Assignment(id=id_, executor_id='1', role_id='1')

    assert assignment.id == id_
    assert assignment.executor_id == executor_id
    assert assignment.role_id == role_id
