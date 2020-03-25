from ...application.models import Task
from ...application.utilities import QueryParser
from ...application.repositories import TaskRepository
from .rst_repository import RstRepository, RstLoader


class RstTaskRepository(RstRepository[Task], TaskRepository):
    """Restructuredtext Task Repository"""

    def __init__(self, parser: QueryParser,
                 loader: RstLoader) -> None:
        super().__init__(parser=parser, loader=loader, item_class=Task)
