from pytest import fixture
from estimark.application.domain.models import Classification
from estimark.application.domain.common import QueryParser
from estimark.core.data import RstClassificationRepository


@fixture
def rst_classification_repository(rst_loader) -> RstClassificationRepository:
    parser = QueryParser()
    repository = RstClassificationRepository(parser, rst_loader)
    return repository


def test_rst_classification_repository_instantiation(
        rst_classification_repository) -> None:
    assert rst_classification_repository is not None
    assert rst_classification_repository.item_class is Classification
