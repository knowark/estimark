from typing import Dict
from pytest import fixture, raises
from estimark.application.models import Classification
from estimark.application.utilities import QueryParser
from estimark.infrastructure.data import RstLoader
from estimark.infrastructure.data import RstClassificationRepository


@fixture
def rst_classification_repository(rst_loader) -> RstClassificationRepository:
    parser = QueryParser()
    repository = RstClassificationRepository(parser, rst_loader)
    return repository


def test_rst_classification_repository_instantiation(
        rst_classification_repository) -> None:
    assert rst_classification_repository is not None
    assert rst_classification_repository.item_class is Classification
