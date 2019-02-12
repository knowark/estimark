from ..config import Config
from ...application.repositories import ExpressionParser
from ..data import RstRepository, RstTaskRepository, RstAnalyzer
from .standard_factory import StandardFactory


class RstFactory(StandardFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def rst_analyzer(self):
        return RstAnalyzer()

    def rst_task_repository(self, expression_parser: ExpressionParser,
                            analyzer: RstAnalyzer) -> RstTaskRepository:
        root = self.config.get('root', '.')

        print('ROOT>>>>', root)
        return RstTaskRepository(root, expression_parser, analyzer)
