from typing import Dict
from pytest import fixture, raises
from estimark.application.models import Task
from estimark.application.repositories import ExpressionParser
from estimark.infrastructure.data import RstLoader
from estimark.infrastructure.data import RstTaskRepository


@fixture
def rst_task_repository(rst_loader) -> RstTaskRepository:
    parser = ExpressionParser()
    repository = RstTaskRepository(parser, rst_loader)
    return repository


def test_rst_repository_instantiation(rst_task_repository) -> None:
    assert rst_task_repository is not None
    assert rst_task_repository.item_class is Task
