from ..models import Slot
from .repository import Repository
from .memory_repository import MemoryRepository


class SlotRepository(Repository[Slot]):
    """Slot Repository"""


class MemorySlotRepository(
        MemoryRepository[Slot], SlotRepository):
    """Memory Slot Repository"""
