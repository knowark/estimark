from ..config import Config
from ...application.utilities import QueryParser
from ..data.json import (
    init_json_database, JsonRepository, JsonClassifierRepository,
    JsonSlotRepository, JsonScheduleRepository)
from ..core import JsonSetupSupplier
from .altair_factory import AltairFactory


class JsonFactory(AltairFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config
        self.param_dir = self.config.get('param_dir')
        self.result_dir = self.config.get('result_dir')

    def json_classifier_repository(self, query_parser: QueryParser,
                                   ) -> JsonClassifierRepository:
        repository = JsonClassifierRepository(
            self.param_dir, query_parser, file_suffix='param')
        return repository

    def json_schedule_repository(self, query_parser: QueryParser,
                                 ) -> JsonScheduleRepository:
        repository = JsonScheduleRepository(
            self.result_dir, query_parser, file_suffix='result')
        return repository

    def json_slot_repository(self, query_parser: QueryParser,
                             ) -> JsonSlotRepository:
        repository = JsonSlotRepository(
            self.result_dir, query_parser, file_suffix='result')
        return repository

    def json_setup_supplier(self) -> JsonSetupSupplier:
        return JsonSetupSupplier(self.result_dir)
