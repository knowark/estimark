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

        for key, value in nodes.items():
            _id = self._extract_id(value)
            value['id'] = _id
            value['parent_id'] = self._extract_parent_id(value)
            item = self.item_class(**value)
            self.items[_id] = item

    def _extract_id(self, value: Dict[str, Any]) -> str:
        _id = value.get('id', '')
        if _id:
            return _id

        file_name = value.get('file_name', '')
        parent_dir = value.get('parent_dir', '')

        if '_' in file_name:
            _id, *rest = file_name.split('_')
        elif '_' in parent_dir:
            _id, *rest = parent_dir.split('_')

        return _id

    def _extract_parent_id(self, value: Dict[str, Any]) -> str:
        nodes = self.loader.nodes
        parent_value = nodes.get(value.get('parent_absolute'))
        if not parent_value:
            return ''

        return self._extract_id(parent_value)
