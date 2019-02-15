from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict, Type, Callable, Optional, Generic, Tuple, Any
from ...application.repositories import (
    T, QueryDomain, ExpressionParser, Repository)
from .rst_analyzer import RstAnalyzer
from .rst_loader import RstLoader


class RstRepository(Repository, Generic[T]):
    def __init__(self, parser: ExpressionParser,
                 loader: RstLoader,
                 item_class: Type[T]) -> None:
        self.items: Dict[str, Any] = {}
        self.parser = parser
        self.loader = loader
        self.item_class: Callable[..., T] = item_class

    def get(self, id: str) -> Optional[T]:
        return self.items.get(id)

    def add(self, item: T) -> T:
        raise NotImplementedError('Implementation not available.')

    def search(self, domain: QueryDomain, limit=0, offset=0) -> List[T]:
        items = []
        limit = int(limit) if limit > 0 else 100
        offset = int(offset) if offset > 0 else 0
        filter_function = self.parser.parse(domain)
        for item in list(self.items.values()):
            if filter_function(item):
                items.append(item)

        items = items[:limit]
        items = items[offset:]

        return items

    def remove(self, item: T) -> bool:
        raise NotImplementedError('Implementation not available.')

    def load(self):
        nodes = self.loader.nodes

        for value in nodes:
            item = self.item_class(**value)
            self.items[value['id']] = item
