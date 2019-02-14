from ..models import Link
from .repository import Repository
from .memory_repository import MemoryRepository


class LinkRepository(Repository[Link]):
    """Link Repository"""


class MemoryLinkRepository(
        MemoryRepository[Link], LinkRepository):
    """Memory Link Repository"""
