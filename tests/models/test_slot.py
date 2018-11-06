from estimark.application.models import Slot


def test_slot_instantiation():
    slot = Slot(id='SL001', task_id='T001', schedule_id='S001',
                start='2018-11-06T08:00', end='2018-11-06T12:00',
                executor_id='jdacevedo',)

    assert slot.id == 'SL001'
    assert slot.schedule_id == 'S001'
    assert slot.task_id == 'T001'
    assert slot.start == '2018-11-06T08:00'
    assert slot.end == '2018-11-06T12:00'
    assert slot.executor_id == 'jdacevedo'
