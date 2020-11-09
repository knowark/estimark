from pytest import raises
from estimark.application.domain.models import Schedule, Task


def test_estimation_manager_instantiation(estimation_manager):
    assert estimation_manager is not None


def test_estimation_manager_calculate_slots(estimation_manager):
    slots = estimation_manager._calculate_slots()
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


def test_estimation_manager_estimate(estimation_manager):
    estimation_manager.estimate()
    assert len(
        estimation_manager.schedule_repository.data['data']) == 1


def test_estimation_manager_plot_empty(estimation_manager):
    result = estimation_manager.plot()
    assert result is False


def test_estimation_manager_plot_schedule(estimation_manager):
    estimation_manager.schedule_repository.load({'data': {
        '1': Schedule(**{'id': '1', 'name': 'Sample'}),
    }})
    result = estimation_manager.plot('gantt')
    assert result is True
    assert getattr(estimation_manager.plot_service,
                   'gantt_plotted') is True


def test_estimation_manager_estimate_merged_tasks(
        estimation_manager, merged_link_repository):
    estimation_manager.link_repository = merged_link_repository
    slots = estimation_manager._calculate_slots()
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


def test_estimation_manager_calculate_slots_state_missing(
        estimation_manager):
    states = ['missing']
    slots = estimation_manager._calculate_slots(states=states)
    assert slots == []


def test_estimation_manager_plot_kanban(estimation_manager):
    result = estimation_manager.plot('kanban')
    assert result is True
    assert getattr(estimation_manager.plot_service,
                   'kanban_plotted') is True


def test_estimation_manager_plot_kanban_no_tasks(estimation_manager):
    estimation_manager.task_repository.load({'data': {}})
    result = estimation_manager.plot('kanban')
    assert result is False
    assert getattr(estimation_manager.plot_service,
                   'kanban_plotted') is False


def test_estimation_manager_plot_kanban_states(estimation_manager):
    context = {'states': ['backlog']}
    result = estimation_manager.plot('kanban', context)
    assert result is True
    assert getattr(estimation_manager.plot_service,
                   'kanban_plotted') is True


def test_estimation_manager_plot_kanban_owners(estimation_manager):
    context = {'owners': ['unassigned']}
    result = estimation_manager.plot('kanban', context)
    assert result is True
    assert getattr(estimation_manager.plot_service,
                   'kanban_plotted') is True


def test_estimation_manager_plot_invalid_type(estimation_manager):
    with raises(ValueError):
        estimation_manager.plot('invalid')
