from pytest import fixture
from pathlib import Path
from estimark.application.domain.models import Schedule, Slot, Task
from estimark.application.domain.common import QueryParser
from estimark.application.domain.repositories import MemorySlotRepository
from estimark.core.plot import AltairPlotService


@fixture
def slot_repository():
    slot_repository = MemorySlotRepository(QueryParser())
    slot_repository.load({'data': {
        '1.1':  Slot(id='1.1', schedule_id='1',
                     task_id='1.1', start=0, end=3),
        '1.2':  Slot(id='1.2', schedule_id='1',
                     task_id='1.2', start=3, end=8),
        '1.3':  Slot(id='1.3', schedule_id='1',
                     task_id='1.3', start=8, end=10)
    }})

    return slot_repository


@fixture
def plot_service(slot_repository):
    return AltairPlotService('/tmp', slot_repository)


def test_altair_plot_service_plot_gantt(plot_service, tmpdir):
    output_file = str(tmpdir / 'gantt.html')
    plot_service.plot_dir = str(tmpdir)

    schedule = Schedule(id='1', name='Test Schedule')

    plot_service.plot_gantt(schedule)

    assert len(Path(output_file).read_bytes()) > 0


def test_altair_plot_service_plot_kanban(plot_service, tmpdir):
    output_file = str(tmpdir / 'kanban.html')
    plot_service.plot_dir = str(tmpdir)

    tasks = [Task(id='001', state='backlog'), Task(id='002', state='open')]

    plot_service.plot_kanban(tasks)

    assert len(Path(output_file).read_bytes()) > 0
