from estimark.application.models import Classifier, Schedule, Slot
from estimark.application.utilities import QueryParser
from estimark.application.repositories import (
    ClassifierRepository, ScheduleRepository, SlotRepository)
from estimark.infrastructure.data.json import JsonRepository


class JsonClassifierRepository(
        JsonRepository[Classifier], ClassifierRepository):
    """Json Classifier Repository"""

    def __init__(self, file_path: str, parser: QueryParser,
                 collection_name: str = 'classifiers') -> None:
        super().__init__(file_path, parser, collection_name, Classifier)


class JsonScheduleRepository(
        JsonRepository[Schedule], ScheduleRepository):
    """Json Schedule Repository"""

    def __init__(self, file_path: str, parser: QueryParser,
                 collection_name: str = 'schedules') -> None:
        super().__init__(file_path, parser, collection_name, Schedule)


class JsonSlotRepository(
        JsonRepository[Slot], SlotRepository):
    """Json Slot Repository"""

    def __init__(self, file_path: str, parser: QueryParser,
                 collection_name: str = 'slots') -> None:
        super().__init__(file_path, parser, collection_name, Slot)
