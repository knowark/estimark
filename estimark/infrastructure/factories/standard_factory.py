from ..config import Config
from ...application.utilities import QueryParser
from ...application.repositories import (
    TaskRepository, MemoryTaskRepository,
    LinkRepository, MemoryLinkRepository,
    ClassifierRepository, MemoryClassifierRepository,
    ClassificationRepository, MemoryClassificationRepository,
    ScheduleRepository, MemoryScheduleRepository,
    SlotRepository, MemorySlotRepository)
from ...application.services import PlotService, MemoryPlotService
from ...application.coordinators import EstimationCoordinator
from ...application.informers import (
    EstimarkInformer, StandardEstimarkInformer)
from .factory import Factory


class StandardFactory(Factory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config

    def extract(self, method: str):
        return getattr(self, "{0}".format(method), None)

    def query_parser(self) -> QueryParser:
        return QueryParser()

    def memory_task_repository(
            self, query_parser: QueryParser
    ) -> MemoryTaskRepository:
        return MemoryTaskRepository(query_parser)

    def memory_link_repository(
            self, query_parser: QueryParser
    ) -> MemoryLinkRepository:
        return MemoryLinkRepository(query_parser)

    def memory_classifier_repository(
            self, query_parser: QueryParser
    ) -> MemoryClassifierRepository:
        return MemoryClassifierRepository(query_parser)

    def memory_classification_repository(
            self, query_parser: QueryParser
    ) -> MemoryClassificationRepository:
        return MemoryClassificationRepository(query_parser)

    def memory_schedule_repository(
            self, query_parser: QueryParser
    ) -> MemoryScheduleRepository:
        return MemoryScheduleRepository(query_parser)

    def memory_slot_repository(
            self, query_parser: QueryParser
    ) -> MemorySlotRepository:
        return MemorySlotRepository(query_parser)

    def memory_plot_service(
            self, slot_repository: SlotRepository
    ) -> MemoryPlotService:
        return MemoryPlotService(slot_repository)

    def estimation_coordinator(
            self, task_repository: TaskRepository,
            classifier_repository: ClassifierRepository,
            classification_repository: ClassificationRepository,
            link_repository: LinkRepository,
            schedule_repository: ScheduleRepository,
            slot_repository: SlotRepository,
            plot_service: PlotService
    ) -> EstimationCoordinator:
        return EstimationCoordinator(
            task_repository, classifier_repository,
            classification_repository, link_repository,
            schedule_repository, slot_repository, plot_service)

    def standard_estimark_informer(
            self, task_repository: TaskRepository,
            link_repository: LinkRepository,
            classifier_repository: ClassifierRepository,
            schedule_repository: ScheduleRepository,
            slot_repository: SlotRepository
    ) -> StandardEstimarkInformer:
        return StandardEstimarkInformer(
            task_repository, link_repository, classifier_repository,
            schedule_repository, slot_repository)
