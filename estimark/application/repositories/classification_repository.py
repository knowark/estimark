from ..models import Classification
from .repository import Repository
from .memory_repository import MemoryRepository


class ClassificationRepository(Repository[Classification]):
    """Classification Repository"""


class MemoryClassificationRepository(
        MemoryRepository[Classification], ClassificationRepository):
    """Memory Classification Repository"""
