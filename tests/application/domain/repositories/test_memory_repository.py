from time import sleep
from pytest import fixture
from estimark.application.domain.common import (
    QueryParser)
from estimark.application.domain.models import Entity
from estimark.application.domain.repositories import (
    Repository, MemoryRepository)


class DummyEntity(Entity):
    def __init__(self, **attributes) -> None:
        super().__init__(**attributes)
        self.field_1 = attributes.get('field_1', "")


def test_memory_repository_implementation() -> None:
    assert issubclass(MemoryRepository, Repository)


@fixture
def memory_repository() -> MemoryRepository:
    parser = QueryParser()
    repository: MemoryRepository = MemoryRepository(parser)
    repository.load({"default": {}})
    return repository


@fixture
def filled_memory_repository(memory_repository) -> MemoryRepository:
    data_dict = {
        "default": {
            "1": DummyEntity(id='1', field_1='value_1'),
            "2": DummyEntity(id='2', field_1='value_2'),
            "3": DummyEntity(id='3', field_1='value_3')
        }
    }
    memory_repository.load(data_dict)
    return memory_repository


def test_memory_repository_add(memory_repository) -> None:
    item = DummyEntity(id="1", field_1="value_1")

    is_saved = memory_repository.add(item)

    assert len(memory_repository.data['default']) == 1
    assert is_saved
    assert "1" in memory_repository.data['default'].keys()
    assert item in memory_repository.data['default'].values()


def test_memory_repository_add_update(memory_repository) -> None:
    created_entity = DummyEntity(id="1", field_1="value_1")
    created_entity, *_ = memory_repository.add(created_entity)

    sleep(1)

    updated_entity = DummyEntity(id="1", field_1="New Value")
    updated_entity, *_ = memory_repository.add(updated_entity)

    assert created_entity.created_at == updated_entity.created_at

    items = memory_repository.data['default']
    assert len(items) == 1
    assert "1" in items.keys()
    assert updated_entity in items.values()
    assert "New Value" in items['1'].field_1


def test_memory_repository_add_no_id(memory_repository) -> None:
    item = DummyEntity(field_1="value_1")

    is_saved = memory_repository.add(item)

    items = memory_repository.data['default']
    assert len(items) == 1
    assert is_saved
    assert len(list(items.keys())[0]) > 0
    assert item in items.values()


def test_memory_repository_search(filled_memory_repository):
    domain = [('field_1', '=', "value_3")]

    items = filled_memory_repository.search(domain)

    assert len(items) == 1
    for item in items:
        assert item.id == '3'
        assert item.field_1 == "value_3"


def test_memory_repository_search_all(filled_memory_repository):
    items = filled_memory_repository.search([])

    assert len(items) == 3


def test_memory_repository_count(filled_memory_repository):
    count = filled_memory_repository.count()

    assert count == 3


def test_memory_repository_count_domain(filled_memory_repository):
    domain = [('field_1', '=', "value_3")]
    count = filled_memory_repository.count(domain)

    assert count == 1


def test_memory_repository_search_limit(filled_memory_repository):
    items = filled_memory_repository.search([], limit=2)

    assert len(items) == 2


def test_memory_repository_search_limit_none(filled_memory_repository):
    items = filled_memory_repository.search([], limit=None, offset=None)

    assert len(items) == 3


def test_memory_repository_search_offset(filled_memory_repository):
    items = filled_memory_repository.search([], offset=2)

    assert len(items) == 1


def test_memory_repository_remove_true(filled_memory_repository):
    item = filled_memory_repository.data['default']["2"]
    deleted = filled_memory_repository.remove(item)

    items = filled_memory_repository.data['default']
    assert deleted is True
    assert len(items) == 2
    assert "2" not in items


def test_memory_repository_remove_false(filled_memory_repository):
    item = DummyEntity(**{'id': '6', 'field_1': 'MISSING'})
    deleted = filled_memory_repository.remove(item)

    items = filled_memory_repository.data['default']
    assert deleted is False
    assert len(items) == 3


def test_memory_repository_remove_idempotent(filled_memory_repository):
    existing_item = item = filled_memory_repository.data['default']["2"]
    missing_item = DummyEntity(**{'id': '6', 'field_1': 'MISSING'})

    items = filled_memory_repository.data['default']

    deleted = filled_memory_repository.remove(
        [existing_item, missing_item])

    assert deleted is True
    assert len(items) == 2

    deleted = filled_memory_repository.remove(
        [existing_item, missing_item])

    assert deleted is False
    assert len(items) == 2


def test_memory_repository_add_multiple(memory_repository) -> None:
    items = [
        DummyEntity(field_1="value_1"),
        DummyEntity(field_1="value_2")
    ]

    returned_items = memory_repository.add(items)

    items = memory_repository.data['default']
    assert len(returned_items) == 2
    assert returned_items[0].field_1 == 'value_1'
    assert returned_items[1].field_1 == 'value_2'
