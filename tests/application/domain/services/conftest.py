from pytest import fixture
from estimark.application.domain.common import QueryParser
from estimark.application.domain.repositories import MemorySlotRepository
from estimark.application.domain.services import MemoryPlotService


@fixture
def slot_repository():
    return MemorySlotRepository(QueryParser())


@fixture
def plot_service():
    return MemoryPlotService()
