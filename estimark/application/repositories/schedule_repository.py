from ..models import Schedule
from .repository import Repository
from .memory_repository import MemoryRepository


class ScheduleRepository(Repository[Schedule]):
    """Schedule Repository"""


class MemoryScheduleRepository(
        MemoryRepository[Schedule], ScheduleRepository):
    """Memory Schedule Repository"""
