import os
import time
from json import load, dump
from uuid import uuid4
from typing import Dict, List, Union, Any, Type, TypeVar, Callable, Generic
from ....application.utilities import QueryParser
from ....application.repositories import Repository, QueryDomain


T = TypeVar('T')


class JsonRepository(Repository, Generic[T]):
    def __init__(self, directory_path: str, parser: QueryParser,
                 collection_name: str, item_class: Type[T],
                 file_suffix: str = '') -> None:
        self.directory_path = directory_path
        self.parser = parser
        self.collection_name = collection_name
        self.item_class = item_class  # type: Callable[..., T]
        self.file_suffix = file_suffix
        self.max_items = 10_000

    def add(self, item: Union[T, List[T]]) -> List[T]:
        items = item if isinstance(item, list) else [item]
        data = {}  # type: Dict[str, Any]
        with open(self.file_path, 'r') as f:
            data = load(f)

        for item in items:
            item.id = item.id or str(uuid4())
            item.updated_at = int(time.time())
            if not data[self.collection_name].get(item.id):
                item.created_at = item.updated_at

            data[self.collection_name][item.id] = vars(item)

        with open(self.file_path, 'w') as f:
            dump(data, f, indent=2)

        return items

    def search(self, domain: QueryDomain,
               limit=10_000, offset=0) -> List[T]:
        with open(self.file_path, 'r') as f:
            data = load(f)
            items_dict = data.get(self.collection_name, {})

        items = []
        filter_function = self.parser.parse(domain)
        for item_dict in items_dict.values():
            item = self.item_class(**item_dict)
            if filter_function(item):
                items.append(item)

        if offset is not None:
            items = items[offset:]

        if limit is not None:
            items = items[:min(limit, self.max_items)]

        return items

    def remove(self, item: Union[T, List[T]]) -> bool:
        items = item if isinstance(item, list) else [item]
        with open(self.file_path, 'r') as f:
            data = load(f)

        deleted = False
        for item in items:
            deleted_item = data[self.collection_name].pop(item.id, None)
            deleted = bool(deleted_item) or deleted

        with open(self.file_path, 'w') as f:
            dump(data, f)

        return deleted

    def count(self, domain: QueryDomain = None) -> int:
        with open(self.file_path, 'r') as f:
            data = load(f)

        count = 0
        domain = domain or []
        filter_function = self.parser.parse(domain)
        for item_dict in list(data[self.collection_name].values()):
            item = self.item_class(**item_dict)
            if filter_function(item):
                count += 1
        return count

    @property
    def _location(self) -> str:
        return 'default'

    @property
    def file_path(self) -> str:
        file_path = f'{self.directory_path}/{self._location}'
        if self.file_suffix:
            file_path = f'{file_path}_{self.file_suffix}'
        return f'{file_path}.json'
