from json import dumps, loads
from pytest import fixture
from estimark.application.repositories import Repository, ExpressionParser
from estimark.infrastructure.data.json import JsonRepository


class DummyEntity:
    def __init__(self, id: str = '', field_1: str = '') -> None:
        self.id = id
        self.field_1 = field_1


def test_json_repository_implementation() -> None:
    assert issubclass(JsonRepository, Repository)


@fixture
def json_repository(tmpdir) -> JsonRepository:
    item_dict = {
        "1": vars(DummyEntity('1', 'value_1')),
        "2": vars(DummyEntity('2', 'value_2')),
        "3": vars(DummyEntity('3', 'value_3'))
    }

    file_path = str(tmpdir.mkdir("authark").join('authark_data.json'))
    collection_name = 'dummies'
    with open(file_path, 'w') as f:
        data = dumps({collection_name: item_dict})
        f.write(data)

    parser = ExpressionParser()
    json_repository = JsonRepository(file_path=file_path,
                                     parser=parser,
                                     collection_name=collection_name,
                                     item_class=DummyEntity)
    return json_repository


def test_json_repository_get(json_repository):
    item = json_repository.get("1")
    assert item and item.field_1 == "value_1"


def test_json_repository_get_not_found(json_repository):
    item = json_repository.get("99")
    assert item is None


def test_json_repository_add(json_repository):
    item = DummyEntity('5', 'value_5')
    json_repository.add(item)

    file_path = json_repository.file_path
    with open(file_path) as f:
        data = loads(f.read())
        items = data.get("dummies")

        item_dict = items.get('5')

        assert item_dict.get('field_1') == item.field_1


def test_json_repository_add_no_id(json_repository) -> None:
    item = DummyEntity(field_1='value_5')
    item = json_repository.add(item)

    file_path = json_repository.file_path
    with open(file_path) as f:
        data = loads(f.read())
        items = data.get("dummies")
        for key in items:
            assert len(key) > 0


def test_json_repository_update(json_repository) -> None:
    updated_entity = DummyEntity("1", "New Value")

    is_updated = json_repository.update(updated_entity)

    file_path = json_repository.file_path
    with open(file_path) as f:
        data = loads(f.read())
        items = data.get("dummies")

        assert len(items) == 3
        assert is_updated is True
        assert "New Value" in items['1']['field_1']


def test_json_repository_update_false(json_repository):
    missing_entity = DummyEntity("99", "New Value")

    is_updated = json_repository.update(missing_entity)

    file_path = json_repository.file_path
    with open(file_path) as f:
        data = loads(f.read())
        items = data.get("dummies")

        assert len(items) == 3
        assert is_updated is False


def test_json_repository_search(json_repository):
    domain = [('field_1', '=', "value_3")]
    items = json_repository.search(domain)

    assert len(items) == 1
    for item in items:
        assert item.id == '3'
        assert item.field_1 == "value_3"


def test_json_repository_search_all(json_repository):
    items = json_repository.search([])
    assert len(items) == 3


def test_json_repository_search_limit(json_repository):
    items = json_repository.search([], limit=2)
    assert len(items) == 2


def test_json_repository_search_limit_zero(json_repository):
    items = json_repository.search([], limit=0)
    assert len(items) == 3


def test_json_repository_search_offset(json_repository):
    items = json_repository.search([], offset=2)
    assert len(items) == 1


def test_json_repository_remove_true(json_repository):
    file_path = json_repository.file_path
    with open(file_path) as f:
        data = loads(f.read())
        items_dict = data.get("dummies")
        item_dict = items_dict.get('2')

    item = DummyEntity(**item_dict)
    deleted = json_repository.remove(item)

    with open(file_path) as f:
        data = loads(f.read())
        items_dict = data.get("dummies")

    assert deleted is True
    assert len(items_dict) == 2
    assert "2" not in items_dict.keys()


def test_json_repository_remove_false(json_repository):
    file_path = json_repository.file_path
    item = DummyEntity(**{'id': '6', 'field_1': 'MISSING'})
    deleted = json_repository.remove(item)

    with open(file_path) as f:
        data = loads(f.read())
        items_dict = data.get("dummies")

    assert deleted is False
    assert len(items_dict) == 3
