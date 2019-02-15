from ..config import Config
from ...application.repositories import (
    ExpressionParser, TaskRepository, MemoryTaskRepository,
    LinkRepository, MemoryLinkRepository)
from ...application.coordinators import EstimationCoordinator
from ...application.informers import (
    EstimarkInformer, StandardEstimarkInformer)
from .factory import Factory


class StandardFactory(Factory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def extract(self, method: str):
        return getattr(self, "{0}".format(method), None)

    def expression_parser(self) -> ExpressionParser:
        return ExpressionParser()

    def memory_task_repository(
            self, expression_parser: ExpressionParser
    ) -> MemoryTaskRepository:
        return MemoryTaskRepository(expression_parser)

    def memory_link_repository(
            self, expression_parser: ExpressionParser
    ) -> MemoryLinkRepository:
        return MemoryLinkRepository(expression_parser)

    def estimation_coordinator(
            self, task_repository: TaskRepository
    ) -> EstimationCoordinator:
        return EstimationCoordinator(task_repository)

    def standard_estimark_informer(
            self, task_repository: TaskRepository,
            link_repository: LinkRepository
    ) -> StandardEstimarkInformer:
        return StandardEstimarkInformer(task_repository, link_repository)
