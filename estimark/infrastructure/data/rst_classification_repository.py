from ...application.models import Classification
from ...application.repositories import (ClassificationRepository,
                                         ExpressionParser)
from .rst_repository import RstRepository, RstLoader


class RstClassificationRepository(
        RstRepository[Classification], ClassificationRepository):
    """Restructuredtext Classification Repository"""

    def __init__(self, parser: ExpressionParser,
                 loader: RstLoader) -> None:
        super().__init__(parser=parser,
                         loader=loader, item_class=Classification)
        self.counter = 0

    def load(self):
        for value in self.loader.nodes:
            classifier_ids = value.get('classifiers', [])
            if isinstance(classifier_ids, str):
                classifier_ids = [classifier_ids]

            for classifier_id in classifier_ids:
                self.counter += 1
                item = self.item_class(
                    **{'id': self.counter,
                        'classifier_id': classifier_id,
                       'task_id': value['id']})
                self.items[self.counter] = item
