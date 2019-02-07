from abc import ABC, abstractmethod
from typing import List, Dict, TypeVar, Optional, Generic, Union
from ...application.repositories import (
    T, QueryDomain, ExpressionParser, Repository)


class RstRepository(Repository, Generic[T]):
    pass
