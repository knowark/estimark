import os
from json import load, dump
from uuid import uuid4
from typing import Dict, List, Union, Any, Type, TypeVar, Callable, Generic
from ....application.utilities import QueryParser
from ....application.repositories import Repository, QueryDomain


T = TypeVar('T')


class JsonRepository(Repository, Generic[T]):
    def __init__(self, file_path: str, parser: QueryParser,
                 collection_name: str, item_class: Type[T]) -> None:
        self.file_path = file_path
        self.parser = parser
        self.collection_name = collection_name
        self.item_class = item_class  # type: Callable[..., T]

    def add(self, item: Union[T, List[T]]) -> List[T]:
        data = {}  # type: Dict[str, Any]
        with open(self.file_path, 'r') as f:
            data = load(f)
        setattr(item, 'id', getattr(item, 'id') or str(uuid4()))
        data[self.collection_name].update({getattr(item, 'id'): vars(item)})
        with open(self.file_path, 'w') as f:
            dump(data, f, indent=2)
        return item

    def search(self, domain: QueryDomain, limit=0, offset=0) -> List[T]:
        with open(self.file_path, 'r') as f:
            data = load(f)
            items_dict = data.get(self.collection_name, {})

        items = []
        limit = int(limit) if limit > 0 else 100
        offset = int(offset) if offset > 0 else 0
        filter_function = self.parser.parse(domain)
        for item_dict in items_dict.values():
            item = self.item_class(**item_dict)

            if filter_function(item):
                items.append(item)

        items = items[:limit]
        items = items[offset:]

        return items

    def remove(self, item: T) -> bool:
        with open(self.file_path, 'r') as f:
            data = load(f)
            items_dict = data.get(self.collection_name)

        id = getattr(item, 'id')
        if id not in items_dict:
            return False

        del items_dict[id]

        with open(self.file_path, 'w') as f:
            dump(data, f)
        return True

    def count(self, domain: QueryDomain = None) -> int:
        count = 0
        domain = domain or []
        filter_function = self.parser.parse(domain)
        for item in list(self.data[self._location].values()):
            if filter_function(item):
                count += 1
        return count
