from ...application.models import Link
from ...application.repositories import LinkRepository, ExpressionParser
from .rst_repository import RstRepository, RstLoader


class RstLinkRepository(RstRepository[Link], LinkRepository):
    """Restructuredtext Link Repository"""

    def __init__(self, parser: ExpressionParser,
                 loader: RstLoader) -> None:
        super().__init__(parser=parser, loader=loader, item_class=Link)
        self.counter = 0

    def load(self):
        nodes = self.loader.nodes

        previous = ''
        for value in nodes:
            if value.get('summary'):
                continue

            target = value.get('id')
            predecessors = value.get('predecessors', [])

            if not predecessors:
                predecessors.append(previous)

            for source in predecessors:
                self.counter += 1
                item = self.item_class(
                    id=self.counter, source=source, target=target)
                self.items[self.counter] = item

            previous = target
