from typing import Dict
from pytest import fixture
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


# def test_memory_repository_add() -> None:
#     parser = ExpressionParser()
#     memory_repository = MemoryRepository[DummyEntity](parser)

#     item = DummyEntity("1", "value_1")

#     is_saved = memory_repository.add(item)

#     assert len(memory_repository.items) == 1
#     assert is_saved
#     assert "1" in memory_repository.items.keys()
#     assert item in memory_repository.items.values()


# def test_memory_repository_search(memory_repository):
#     domain = [('field_1', '=', "value_3")]

#     items = memory_repository.search(domain)

#     assert len(items) == 1
#     for item in items:
#         assert item.id == '3'
#         assert item.field_1 == "value_3"


# def test_memory_repository_search_all(memory_repository):
#     items = memory_repository.search([])

#     assert len(items) == 3


# def test_memory_repository_search_limit(memory_repository):
#     items = memory_repository.search([], limit=2)

#     assert len(items) == 2


# def test_memory_repository_search_limit_zero(memory_repository):
#     items = memory_repository.search([], limit=0)

#     assert len(items) == 3


# def test_memory_repository_search_offset(memory_repository):
#     items = memory_repository.search([], offset=2)

#     assert len(items) == 1


# def test_memory_repository_remove_true(memory_repository):
#     item = memory_repository.items["2"]
#     deleted = memory_repository.remove(item)

#     assert deleted is True
#     assert len(memory_repository.items) == 2
#     assert "2" not in memory_repository.items


# def test_memory_repository_remove_false(memory_repository):
#     item = DummyEntity(**{'id': '6', 'field_1': 'MISSING'})
#     deleted = memory_repository.remove(item)

#     assert deleted is False
#     assert len(memory_repository.items) == 3
