from pytest import fixture
from estimark.application.domain.models import Task
from estimark.application.domain.common import QueryParser
from estimark.application.domain.repositories import (
    MemoryTaskRepository, MemoryLinkRepository, MemoryClassifierRepository,
    MemoryScheduleRepository, MemorySlotRepository)
from estimark.application.informers import StandardEstimarkInformer


@fixture
def task_repository():
    memory_task_repository = MemoryTaskRepository(QueryParser())
    memory_task_repository.load({'data': {
        "1": Task(id='1', name='Define WBS'),
        "2": Task(id='2', name='Deploy Servers'),
        "3": Task(id='3', name='Design Website')
    }})
    return memory_task_repository


@fixture
def link_repository():
    return MemoryLinkRepository(QueryParser())


@fixture
def classifier_repository():
    return MemoryClassifierRepository(QueryParser())


@fixture
def schedule_repository():
    return MemoryScheduleRepository(QueryParser())


@fixture
def slot_repository():
    return MemorySlotRepository(QueryParser())


@fixture
def estimark_informer(task_repository, link_repository, classifier_repository,
                      schedule_repository, slot_repository):
    estimark_informer = StandardEstimarkInformer(
        task_repository, link_repository, classifier_repository,
        schedule_repository, slot_repository)
    return estimark_informer
