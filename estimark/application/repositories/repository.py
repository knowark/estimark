from abc import ABC, abstractmethod
from typing import List, Generic, Union, Any
from ..models import T
from ..utilities import QueryDomain


class Repository(ABC, Generic[T]):
    @abstractmethod
    def add(self, item: Union[T, List[T]]) -> List[T]:
        "Add method to be implemented."

    @abstractmethod
    def search(self, domain: QueryDomain,
               limit: int = None, offset: int = None) -> List[T]:
        "Search items matching a query domain"

    @abstractmethod
    def remove(self, item: Union[T, List[T]]) -> bool:
        "Remove method to be implemented."

    @abstractmethod
    def count(self, domain: QueryDomain = None) -> int:
        "Count items matching a query domain"
