from estimark.application.models import Schedule
from estimark.application.repositories import MemorySlotRepository
from estimark.application.services import PlotService


def test_plot_service_instantiation(plot_service):
    assert isinstance(plot_service, PlotService)


def test_plot_service_plot(plot_service):
    schedule = Schedule()

    assert plot_service.plot(schedule) is None
