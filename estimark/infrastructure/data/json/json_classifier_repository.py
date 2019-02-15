from estimark.application.models import Classifier
from estimark.application.repositories import (
    ExpressionParser, ClassifierRepository)
from estimark.infrastructure.data.json import JsonRepository


class JsonClassifierRepository(
        JsonRepository[Classifier], ClassifierRepository):
    """Json Classifier Repository"""

    def __init__(self, file_path: str, parser: ExpressionParser,
                 collection_name: str = 'classifiers') -> None:
        super().__init__(file_path, parser, collection_name, Classifier)
