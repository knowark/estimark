from ..config import Config
from ...application.repositories import (
    ExpressionParser,
    TaskRepository, MemoryTaskRepository)
from ...application.coordinators import EstimationCoordinator
from ...application.informers import (
    EstimarkInformer, StandardEstimarkInformer)


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

    def estimation_coordinator(
            self, task_repository: TaskRepository
    ) -> EstimationCoordinator:
        return EstimationCoordinator(task_repository)

    def standard_estimark_informer(
            self, task_repository: TaskRepository
    ) -> StandardEstimarkInformer:
        return StandardEstimarkInformer(task_repository)
