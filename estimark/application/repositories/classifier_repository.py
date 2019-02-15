from ..models import Classifier
from .repository import Repository
from .memory_repository import MemoryRepository


class ClassifierRepository(Repository[Classifier]):
    """Classifier Repository"""


class MemoryClassifierRepository(
        MemoryRepository[Classifier], ClassifierRepository):
    """Memory Classifier Repository"""
