from typing import Dict
from pytest import fixture, raises
from estimark.application.repositories import Repository, ExpressionParser
from estimark.infrastructure.data import RstRepository, RstAnalyzer


class DummyEntity:
    def __init__(self, **attributes) -> None:
        self.id = attributes.get('id', '')
        self.field_1 = attributes.get('field_1', '')


def test_rst_repository_implementation() -> None:
    assert issubclass(RstRepository, Repository)


@fixture
def rst_repository(root_directory: str) -> RstRepository:
    parser = ExpressionParser()
    analyzer = RstAnalyzer()
    repository = RstRepository[DummyEntity](root_directory, parser,
                                            analyzer, DummyEntity)
    return repository


def test_rst_repository_load(rst_repository) -> None:
    rst_repository.load()
    assert len(rst_repository.items) > 0


def test_rst_repository_get(rst_repository) -> None:
    item = rst_repository.get("2.1.1.1")
    assert item and item.field_1 == "value_1"


def test_rst_repository_add(rst_repository) -> None:
    item = DummyEntity(id="1", field_1="value_1")

    with raises(NotImplementedError):
        rst_repository.add(item)


def test_rst_repository_remove(rst_repository) -> None:
    item = DummyEntity(id="1", field_1="value_1")

    with raises(NotImplementedError):
        rst_repository.remove(item)


def test_rst_repository_search(rst_repository):
    domain = [('field_1', '=', "value_3")]

    items = rst_repository.search(domain)

    assert len(items) == 1
    for item in items:
        assert item.id == '2.1.2.3'
        assert item.field_1 == "value_3"


def test_rst_repository_search_all(rst_repository):
    items = rst_repository.search([])
    assert len(items) > 10


def test_rst_repository_search_limit(rst_repository):
    items = rst_repository.search([], limit=2)
    assert len(items) == 2


def test_rst_repository_search_offset(rst_repository):
    items = rst_repository.search([], offset=2)
    assert len(rst_repository.items) - len(items) == 2