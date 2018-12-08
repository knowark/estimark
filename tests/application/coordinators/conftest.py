from pytest import fixture


@fixture
def estimation_coordinator(trial_registry):
    return trial_registry['EstimationCoordinator']
