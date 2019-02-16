from pytest import fixture
from estimark.application.models import Schedule
from estimark.application.coordinators import EstimationCoordinator


def test_estimation_coordinator_instantiation(estimation_coordinator):
    assert estimation_coordinator is not None


def test_estimation_coordinator_calculate_slots(estimation_coordinator):
    slots = estimation_coordinator._calculate_slots()

    assert len(slots) > 0
    assert slots == [
        {'task_id': '1.1', 'start': 0, 'end': 3},
        {'task_id': '1.2', 'start': 3, 'end': 8},
        {'task_id': '1.3', 'start': 8, 'end': 10},
        {'task_id': '1.4', 'start': 10, 'end': 11},
        {'task_id': '2.1', 'start': 11, 'end': 14},
        {'task_id': '3.1', 'start': 14, 'end': 19},
        {'task_id': '3.2', 'start': 19, 'end': 21},
        {'task_id': '4.1', 'start': 21, 'end': 24},
        {'task_id': '5.1', 'start': 24, 'end': 29},
        {'task_id': '6.1', 'start': 29, 'end': 34},
        {'task_id': '6.2', 'start': 34, 'end': 35},
        {'task_id': '6.3', 'start': 35, 'end': 38},
        {'task_id': '6.4', 'start': 38, 'end': 43},
        {'task_id': '7.1', 'start': 43, 'end': 51}]
