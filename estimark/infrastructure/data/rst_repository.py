from abc import ABC, abstractmethod
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Type, Callable, Optional, Generic, Tuple, Any
from ...application.utilities import QueryParser
from ...application.repositories import (
    T, QueryDomain, Repository)
from .rst_analyzer import RstAnalyzer
from .rst_loader import RstLoader


class RstRepository(Repository, Generic[T]):
    def __init__(self, parser: QueryParser,
                 loader: RstLoader,
                 item_class: Type[T]) -> None:
        self.data: Dict[str, Dict[str, T]] = defaultdict(dict)
        self.parser = parser
        self.loader = loader
        self.item_class: Callable[..., T] = item_class
        self.max_items = 10_000

    def add(self, item: T) -> T:
        raise NotImplementedError('Implementation not available.')

    def search(self, domain: QueryDomain,
               limit=10_000, offset=0) -> List[T]:
        items = []
        filter_function = self.parser.parse(domain)
        for item in list(self.data[self._location].values()):
            if filter_function(item):
                items.append(item)

        if offset is not None:
            items = items[offset:]

        if limit is not None:
            items = items[:min(limit, self.max_items)]

        return items

    def remove(self, item: T) -> bool:
        raise NotImplementedError('Implementation not available.')

    def count(self, domain: QueryDomain = None) -> int:
        count = 0
        domain = domain or []
        filter_function = self.parser.parse(domain)
        for item in list(self.data[self._location].values()):
            if filter_function(item):
                count += 1
        return count

    def load(self):
        for value in self.loader.nodes:
            item = self.item_class(**value)
            self.data[self._location][value['id']] = item

    @property
    def _location(self) -> str:
        return 'default'
