from ...application.models import Task
from ...application.repositories import TaskRepository, ExpressionParser
from .rst_repository import RstRepository, RstAnalyzer


class RstTaskRepository(RstRepository[Task], TaskRepository):
    """Restructuredtext Task Repository"""

    def __init__(self, root: str, parser: ExpressionParser,
                 analyzer: RstAnalyzer) -> None:
        super().__init__(root=root, parser=parser,
                         analyzer=analyzer, item_class=Task)
