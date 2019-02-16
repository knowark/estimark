from ..config import Config
from ...application.repositories import ExpressionParser
from ..data.json import (
    init_json_database, JsonRepository, JsonClassifierRepository,
    JsonSlotRepository, JsonScheduleRepository)
from .standard_factory import StandardFactory


class JsonFactory(StandardFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config
        self.param_path = self.config.get('param')
        self.result_path = self.config.get('result')
        # database_schema = {
        #     'schedules': {},
        #     'slots': {}
        # }
        # init_json_database(self.param_path, database_schema)

    def json_classifier_repository(self, expression_parser: ExpressionParser,
                                   ) -> JsonClassifierRepository:
        repository = JsonClassifierRepository(
            self.param_path, expression_parser)
        return repository

    def json_schedule_repository(self, expression_parser: ExpressionParser,
                                 ) -> JsonScheduleRepository:
        repository = JsonScheduleRepository(
            self.result_path, expression_parser)
        return repository

    def json_slot_repository(self, expression_parser: ExpressionParser,
                             ) -> JsonSlotRepository:
        repository = JsonSlotRepository(
            self.result_path, expression_parser)
        return repository
