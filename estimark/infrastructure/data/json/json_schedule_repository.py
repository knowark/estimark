from estimark.application.models import Schedule
from estimark.application.repositories import (
    ExpressionParser, ScheduleRepository)
from estimark.infrastructure.data.json import JsonRepository


class JsonScheduleRepository(
        JsonRepository[Schedule], ScheduleRepository):
    """Json Schedule Repository"""

    def __init__(self, file_path: str, parser: ExpressionParser,
                 collection_name: str = 'schedules') -> None:
        super().__init__(file_path, parser, collection_name, Schedule)
