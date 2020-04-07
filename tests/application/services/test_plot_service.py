from estimark.application.models import Schedule, Task
from estimark.application.repositories import MemorySlotRepository
from estimark.application.services import PlotService


def test_plot_service_instantiation(plot_service):
    assert isinstance(plot_service, PlotService)


def test_plot_service_plot(plot_service):
    schedule = Schedule()

    assert plot_service.plot(schedule) is None


def test_plot_service_plot_kanban(plot_service):
    tasks = [Task(id='001'), Task(id='002'), Task(id='003')]

    assert plot_service.plot_kanban(tasks) is None
