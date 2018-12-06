from ..models import Task
from .repository import Repository
from .memory_repository import MemoryRepository


class TaskRepository(Repository[Task]):
    """Task Repository"""


class MemoryTaskRepository(
        MemoryRepository[Task], TaskRepository):
    """Memory Task Repository"""
