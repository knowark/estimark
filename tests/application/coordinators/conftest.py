from pytest import fixture
from estimark.application.models import (
    Task, Classifier, Classification, Link, Slot)
from estimark.application.utilities import QueryParser
from estimark.application.repositories import (
    MemoryTaskRepository, MemoryClassifierRepository,
    MemoryClassificationRepository, MemoryLinkRepository,
    MemoryScheduleRepository, MemorySlotRepository)
from estimark.application.services import MemoryPlotService
from estimark.application.coordinators import EstimationCoordinator


@fixture
def classifier_repository():
    classifier_repository = MemoryClassifierRepository(QueryParser())
    classifier_repository.load({'default': {
        "xs": Classifier(**{
            "id": "xs",
            "name": "Extra Small",
            "amount": 1
        }),
        "s": Classifier(**{
            "id": "s",
            "name": "Small",
            "amount": 2
        }),
        "m": Classifier(**{
            "id": "m",
            "name": "Medium",
            "amount": 3
        }),
        "l": Classifier(**{
            "id": "l",
            "name": "Large",
            "amount": 5
        }),
        "xl": Classifier(**{
            "id": "xl",
            "name": "Extra Large",
            "amount": 8
        })
    }})
    return classifier_repository


@fixture
def task_repository():
    task_repository = MemoryTaskRepository(QueryParser())
    task_repository.load({'default': {
        '0': Task(id='', name='Bicycle Project', summary=True, parent_id=''),
        '1': Task(id='1', name='Frame Set', summary=True, parent_id='0'),
        '1.1': Task(id='1.1', name='Make Frame', parent_id='1'),
        '1.2': Task(id='1.2', name='Forge Handlebar', parent_id='1'),
        '1.3': Task(id='1.3', name='Build Fork', parent_id='1'),
        '1.4': Task(id='1.4', name='Make Seat', parent_id='1'),
        '2': Task(id='2', name='Crank Set', summary=True, parent_id='0'),
        '2.1': Task(id='2.1', name='Make Crank Set', parent_id='2'),
        '3': Task(id='3', name='Wheels', summary=True, parent_id='0'),
        '3.1': Task(id='3.1', name='Make Front Wheel', parent_id='3'),
        '3.2': Task(id='3.2', name='Make Rear Wheel', parent_id='3'),
        '4': Task(id='4', name='Braking Systems', summary=True, parent_id='0'),
        '4.1': Task(id='4.1', name='Design Braking Systems', parent_id='4'),
        '5': Task(id='5', name='Shifting Systems',
                  summary=True, parent_id='0'),
        '5.1': Task(id='5.1', name='Design Shifting Systems', parent_id='5'),
        '6': Task(id='6', name='Integration', summary=True, parent_id='0'),
        '6.1': Task(id='6.1', name='Define Concept', parent_id='6'),
        '6.2': Task(id='6.2', name='Draft Design', parent_id='6'),
        '6.3': Task(id='6.3', name='Assembly Parts', parent_id='6'),
        '6.4': Task(id='6.4', name='Make Testing', parent_id='6'),
        '7': Task(id='7', name='Project Management', summary=True,
                  parent_id='0'),
        '7.1': Task(id='7.1', name='Plan Project', parent_id='7')
    }})
    return task_repository


@fixture
def classification_repository():
    classification_repository = MemoryClassificationRepository(
        QueryParser())
    classification_repository.load({'default': {
        "1": Classification(id="1", task_id="1.1", classifier_id="m"),
        "2": Classification(id="2", task_id="1.2", classifier_id="l"),
        "3": Classification(id="3", task_id="1.3", classifier_id="s"),
        "4": Classification(id="4", task_id="1.4", classifier_id="xs"),
        "5": Classification(id="5", task_id="2.1", classifier_id="m"),
        "6": Classification(id="6", task_id="3.1", classifier_id="l"),
        "7": Classification(id="7", task_id="3.2", classifier_id="s"),
        "8": Classification(id="8", task_id="4.1", classifier_id="m"),
        "9": Classification(id="9", task_id="5.1", classifier_id="l"),
        "10": Classification(id="10", task_id="6.1", classifier_id="l"),
        "11": Classification(id="11", task_id="6.2", classifier_id="xs"),
        "12": Classification(id="12", task_id="6.3", classifier_id="m"),
        "13": Classification(id="13", task_id="6.4", classifier_id="l"),
        "14": Classification(id="14", task_id="7.1", classifier_id="xl"),
    }})
    return classification_repository


@fixture
def link_repository():
    link_repository = MemoryLinkRepository(QueryParser())
    link_repository.load({'default': {
        '1': Link(**{'id': '1', 'source': '', 'target': '1.1'}),
        '2': Link(**{'id': '2', 'source': '1.1', 'target': '1.2'}),
        '3': Link(**{'id': '3', 'source': '1.2', 'target': '1.3'}),
        '4': Link(**{'id': '4', 'source': '1.3', 'target': '1.4'}),
        '5': Link(**{'id': '5', 'source': '1.4', 'target': '2.1'}),
        '6': Link(**{'id': '6', 'source': '2.1', 'target': '3.1'}),
        '7': Link(**{'id': '7', 'source': '3.1', 'target': '3.2'}),
        '8': Link(**{'id': '8', 'source': '3.2', 'target': '4.1'}),
        '9': Link(**{'id': '9', 'source': '4.1', 'target': '5.1'}),
        '10': Link(**{'id': '10', 'source': '5.1', 'target': '6.1'}),
        '11': Link(**{'id': '11', 'source': '6.1', 'target': '6.2'}),
        '12': Link(**{'id': '12', 'source': '6.2', 'target': '6.3'}),
        '13': Link(**{'id': '13', 'source': '6.3', 'target': '6.4'}),
        '14': Link(**{'id': '14', 'source': '6.4', 'target': '7.1'}),
    }})
    return link_repository


@fixture
def merged_link_repository():
    link_repository = MemoryLinkRepository(QueryParser())
    link_repository.load({'default': {
        '1': Link(**{'id': '1', 'source': '', 'target': '1.1'}),
        '2': Link(**{'id': '2', 'source': '1.1', 'target': '1.2'}),
        '3': Link(**{'id': '3', 'source': '1.2', 'target': '1.3'}),
        '4': Link(**{'id': '4', 'source': '1.3', 'target': '1.4'}),
        '5': Link(**{'id': '5', 'source': '1.4', 'target': '2.1'}),
        '6': Link(**{'id': '6', 'source': '2.1', 'target': '3.1'}),
        '7': Link(**{'id': '7', 'source': '3.1', 'target': '3.2'}),
        '8': Link(**{'id': '8', 'source': '3.2', 'target': '4.1'}),
        '9': Link(**{'id': '9', 'source': '4.1', 'target': '5.1'}),
        '10': Link(**{'id': '10', 'source': '3.1', 'target': '6.1'}),
        '11': Link(**{'id': '11', 'source': '3.2', 'target': '6.1'}),
        '12': Link(**{'id': '12', 'source': '6.1', 'target': '6.2'}),
        '13': Link(**{'id': '13', 'source': '6.2', 'target': '6.3'}),
        '14': Link(**{'id': '14', 'source': '6.3', 'target': '6.4'}),
        '15': Link(**{'id': '15', 'source': '6.4', 'target': '7.1'}),
    }})
    return link_repository


@fixture
def schedule_repository():
    schedule_repository = MemoryScheduleRepository(QueryParser())
    return schedule_repository


@fixture
def slot_repository():
    slot_repository = MemorySlotRepository(QueryParser())
    return slot_repository


@fixture
def plot_service():
    plot_service = MemoryPlotService()
    return plot_service


@fixture
def estimation_coordinator(task_repository, classifier_repository,
                           classification_repository, link_repository,
                           schedule_repository, slot_repository,
                           plot_service):
    estimation_coordinator = EstimationCoordinator(
        task_repository, classifier_repository, classification_repository,
        link_repository, schedule_repository, slot_repository, plot_service)
    return estimation_coordinator
