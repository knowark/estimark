from pytest import fixture
from estimark.application.coordinators import EstimationCoordinator


@fixture
def estimation_coordinator():
    estimation_coordinator = EstimationCoordinator()
    return estimation_coordinator


def test_estimation_coordinator_instantiation(estimation_coordinator):
    assert estimation_coordinator is not None
