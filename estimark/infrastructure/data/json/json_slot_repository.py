from estimark.application.models import Slot
from estimark.application.repositories import (
    ExpressionParser, SlotRepository)
from estimark.infrastructure.data.json import JsonRepository


class JsonSlotRepository(
        JsonRepository[Slot], SlotRepository):
    """Json Slot Repository"""

    def __init__(self, file_path: str, parser: ExpressionParser,
                 collection_name: str = 'slots') -> None:
        super().__init__(file_path, parser, collection_name, Slot)
