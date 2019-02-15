from ..config import Config
from ...application.repositories import ExpressionParser
from ..data.json import JsonRepository, JsonClassifierRepository
from .standard_factory import StandardFactory


class JsonFactory(StandardFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def json_classifier_repository(self, expression_parser: ExpressionParser,
                                   ) -> JsonClassifierRepository:
        repository = JsonClassifierkRepository(expression_parser)
        repository.load()
        return repository

    # def json_schedule_repository(self, expression_parser: ExpressionParser
    #                              ) -> RstLinkRepository:
    #     repository = RstLinkRepository(expression_parser, loader)
    #     repository.load()
    #     return repository

    # def json_slot_repository(self, expression_parser: ExpressionParser
    #                          ) -> RstLinkRepository:
    #     repository = RstLinkRepository(expression_parser, loader)
    #     repository.load()
    #     return repository
