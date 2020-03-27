from typing import Dict
from pytest import fixture, raises
from estimark.application.utilities import QueryParser
from estimark.application.utilities import QueryParser
from estimark.application.utilities import QueryParser
from estimark.application.repositories import Repository
from estimark.infrastructure.data import RstRepository, RstAnalyzer, RstLoader


class DummyEntity:
    def __init__(self, **attributes) -> None:
        self.id = attributes.get('id', '')
        self.field_1 = attributes.get('field_1', '')


def test_rst_repository_implementation() -> None:
    assert issubclass(RstRepository, Repository)


@fixture
def rst_repository(rst_loader) -> RstRepository:
    parser = QueryParser()
    repository = RstRepository[DummyEntity](
        parser, rst_loader, DummyEntity)
    repository.load()
    return repository


def test_rst_repository_load(rst_repository) -> None:
    rst_repository.load()
    assert len(rst_repository.data['default']) > 0


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
    assert len(rst_repository.data['default']) - len(items) == 2


def test_rst_repository_count(rst_repository):
    count = rst_repository.count()
    assert count == 21


def test_rst_repository_count_domain(rst_repository):
    domain = [('id', '=', "1.1.1")]
    count = rst_repository.count(domain)
    assert count == 1
