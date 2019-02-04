from pytest import fixture


@fixture
def estimation_coordinator(trial_resolver):
    return trial_resolver.resolve('EstimationCoordinator')
