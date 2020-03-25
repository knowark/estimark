from pytest import fixture
from estimark.application.utilities import QueryParser
from estimark.application.repositories import MemorySlotRepository
from estimark.application.services import PlotService, MemoryPlotService


@fixture
def slot_repository():
    return MemorySlotRepository(QueryParser())


@fixture
def plot_service(slot_repository):
    return MemoryPlotService(slot_repository)
