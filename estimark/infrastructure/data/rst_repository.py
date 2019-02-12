from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict, Type, Callable, Optional, Generic, Tuple, Any
from ...application.repositories import (
    T, QueryDomain, ExpressionParser, Repository)
from .rst_analyzer import RstAnalyzer


class RstRepository(Repository, Generic[T]):
    def __init__(self, root: str, parser: ExpressionParser,
                 analyzer: RstAnalyzer, item_class: Type[T]) -> None:
        self.items: Dict[str, Any] = {}
        self.root = root
        self.parser = parser
        self.analyzer = analyzer
        self.item_class: Callable[..., T] = item_class

    def get(self, id: str) -> Optional[T]:
        self.load()
        return self.items.get(id)

    def add(self, item: T) -> T:
        raise NotImplementedError('Implementation not available.')

    def search(self, domain: QueryDomain, limit=0, offset=0) -> List[T]:
        self.load()
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
        path = Path(self.root)
        for node in path.rglob('*.rst'):
            _id, item = self._analyze_node(node)
            self.items[_id] = item

    def _analyze_node(self, node: Path) -> Tuple[str, T]:
        name = node.name
        if name == 'index.rst':
            name = node.parent.name

        _id = self._extract_id(name)
        data_dict = self._extract_content(node)
        data_dict['id'] = _id
        item = self.item_class(**data_dict)
        return _id, item

    def _extract_id(self, name: str) -> str:
        _id = '0'
        if '_' in name:
            _id, *rest = name.split('_')
        return _id

    def _extract_content(self, node: Path) -> Dict[str, Any]:
        content = node.read_text()
        return self.analyzer.analyze(content)
