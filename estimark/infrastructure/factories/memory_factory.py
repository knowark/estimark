from ..config import Config
from ...application.repositories import (
    ExpressionParser,
    TaskRepository, MemoryTaskRepository)


class MemoryFactory:
    def __init__(self, config: Config) -> None:
        self.config = config

    # Repositories

    def expression_parser(self) -> ExpressionParser:
        return ExpressionParser()

    def memory_task_repository(
            self, expression_parser: ExpressionParser
    ) -> MemoryTaskRepository:
        return MemoryTaskRepository(expression_parser)