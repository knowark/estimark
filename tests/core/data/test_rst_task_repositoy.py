from pytest import fixture
from estimark.application.domain.models import Task
from estimark.application.domain.common import QueryParser
from estimark.core.data import RstTaskRepository


@fixture
def rst_task_repository(rst_loader) -> RstTaskRepository:
    parser = QueryParser()
    repository = RstTaskRepository(parser, rst_loader)
    return repository


def test_rst_repository_instantiation(rst_task_repository) -> None:
    assert rst_task_repository is not None
    assert rst_task_repository.item_class is Task
