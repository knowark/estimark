from pytest import fixture
from pathlib import Path
from estimark.application.models import Schedule, Slot
from estimark.application.utilities import QueryParser
from estimark.application.repositories import MemorySlotRepository
from estimark.infrastructure.plot import AltairPlotService


@fixture
def slot_repository():
    slot_repository = MemorySlotRepository(QueryParser())
    slot_repository.load({'default': {
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


def test_altair_plot_service_plot(plot_service, tmpdir):
    output_file = str(tmpdir / 'test_output.html')
    plot_service.output_file = output_file
    schedule = Schedule(id='1', name='Test Schedule')

    plot_service.plot(schedule)

    assert len(Path(output_file).read_bytes()) > 0
