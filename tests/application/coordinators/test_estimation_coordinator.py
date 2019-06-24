from pytest import fixture
from estimark.application.models import Schedule
from estimark.application.coordinators import EstimationCoordinator


def test_estimation_coordinator_instantiation(estimation_coordinator):
    assert estimation_coordinator is not None


def test_estimation_coordinator_calculate_slots(estimation_coordinator):
    slots = estimation_coordinator._calculate_slots()
    expected_slots = {
        '1.1': {'start': 0, 'end': 3},
        '1.2': {'start': 3, 'end': 8},
        '1.3': {'start': 8, 'end': 10},
        '1.4': {'start': 10, 'end': 11},
        '2.1': {'start': 11, 'end': 14},
        '3.1': {'start': 14, 'end': 19},
        '3.2': {'start': 19, 'end': 21},
        '4.1': {'start': 21, 'end': 24},
        '5.1': {'start': 24, 'end': 29},
        '6.1': {'start': 29, 'end': 34},
        '6.2': {'start': 34, 'end': 35},
        '6.3': {'start': 35, 'end': 38},
        '6.4': {'start': 38, 'end': 43},
        '7.1': {'start': 43, 'end': 51}
    }

    assert len(slots) > 0
    for slot in slots:
        expected_slot = expected_slots[slot['task_id']]
        assert slot['start'] == expected_slot['start']
        assert slot['end'] == expected_slot['end']


def test_estimartion_coordinator_estimate(estimation_coordinator):
    estimation_coordinator.estimate()
    assert len(estimation_coordinator.schedule_repository.items) == 1


def test_estimartion_coordinator_estimate_merged_tasks(
        estimation_coordinator, merged_link_repository):
    estimation_coordinator.link_repository = merged_link_repository
    slots = estimation_coordinator._calculate_slots()
    expected_slots = {
        '1.1': {'start': 0, 'end': 3},
        '1.2': {'start': 3, 'end': 8},
        '1.3': {'start': 8, 'end': 10},
        '1.4': {'start': 10, 'end': 11},
        '2.1': {'start': 11, 'end': 14},
        '3.1': {'start': 14, 'end': 19},
        '3.2': {'start': 19, 'end': 21},
        '4.1': {'start': 21, 'end': 24},
        '5.1': {'start': 24, 'end': 29},
        '6.1': {'start': 21, 'end': 26},
        '6.2': {'start': 26, 'end': 27},
        '6.3': {'start': 27, 'end': 30},
        '6.4': {'start': 30, 'end': 35},
        '7.1': {'start': 35, 'end': 43}
    }

    assert len(slots) > 0
    for slot in slots:
        expected_slot = expected_slots[slot['task_id']]
        assert slot['start'] == expected_slot['start']
        assert slot['end'] == expected_slot['end']
