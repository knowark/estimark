from estimark.infrastructure.data import RstAnalyzer


def test_rst_analyzer_definition(rst_analyzer) -> None:
    assert rst_analyzer is not None


# def test_memory_repository_get(memory_repository) -> None:
#     item = memory_repository.get("1")

#     assert item and item.field_1 == "value_1"


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
