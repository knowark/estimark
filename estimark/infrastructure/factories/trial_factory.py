from ..config import Config
from .memory_factory import MemoryFactory
from ...application.models import Task
from ...application.repositories import (
    ExpressionParser,
    TaskRepository, MemoryTaskRepository)


class TrialFactory(MemoryFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    # Repositories
    def memory_task_repository(
            self, expression_parser: ExpressionParser
    ) -> MemoryTaskRepository:

        memory_task_repository = super().memory_task_repository(
            expression_parser)

        memory_task_repository.load({
            "1": Task(id='1', name='Define WBS'),
            "2": Task(id='2', name='Deploy Servers'),
            "3": Task(id='3', name='Design Website')
        })
        return MemoryTaskRepository(expression_parser)