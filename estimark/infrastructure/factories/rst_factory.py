from ..config import Config
from ...application.repositories import ExpressionParser
from ..data import (
    RstRepository, RstTaskRepository, RstLinkRepository,
    RstAnalyzer, RstLoader)
from .standard_factory import StandardFactory


class RstFactory(StandardFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def rst_analyzer(self):
        return RstAnalyzer()

    def rst_loader(self, analyzer: RstAnalyzer):
        root = self.config.get('root', '.')
        return RstLoader(root, analyzer)

    def rst_task_repository(self, expression_parser: ExpressionParser,
                            loader: RstLoader) -> RstTaskRepository:
        repository = RstTaskRepository(expression_parser, loader)
        repository.load()
        return repository

    def rst_link_repository(self, expression_parser: ExpressionParser,
                            loader: RstLoader) -> RstLinkRepository:
        repository = RstLinkRepository(expression_parser, loader)
        repository.load()
        return repository
