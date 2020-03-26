from ..config import Config
from ...application.utilities import QueryParser
from ..data.json import (
    init_json_database, JsonRepository, JsonClassifierRepository,
    JsonSlotRepository, JsonScheduleRepository)
from .altair_factory import AltairFactory


class JsonFactory(AltairFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config
        self.param_path = self.config.get('param')
        self.result_path = self.config.get('result')

    def json_classifier_repository(self, query_parser: QueryParser,
                                   ) -> JsonClassifierRepository:
        repository = JsonClassifierRepository(
            self.param_path, query_parser)
        return repository

    def json_schedule_repository(self, query_parser: QueryParser,
                                 ) -> JsonScheduleRepository:
        repository = JsonScheduleRepository(
            self.result_path, query_parser)
        return repository

    def json_slot_repository(self, query_parser: QueryParser,
                             ) -> JsonSlotRepository:
        repository = JsonSlotRepository(
            self.result_path, query_parser)
        return repository
