from ...application.models import Task
from ...application.repositories import TaskRepository, ExpressionParser
from .rst_repository import RstRepository, RstLoader


class RstTaskRepository(RstRepository[Task], TaskRepository):
    """Restructuredtext Task Repository"""

    def __init__(self, parser: ExpressionParser,
                 loader: RstLoader) -> None:
        super().__init__(parser=parser, loader=loader, item_class=Task)
