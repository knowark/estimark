from abc import ABC, abstractmethod
from ..repositories import (
    TaskRepository, LinkRepository, ClassifierRepository,
    ScheduleRepository, SlotRepository)
from .types import SearchDomain, RecordsList


class EstimarkInformer(ABC):

    @abstractmethod
    def search_tasks(self, domain: SearchDomain) -> RecordsList:
        """Search tasks method to be implemented"""

    @abstractmethod
    def search_links(self, domain: SearchDomain) -> RecordsList:
        """Search links method to be implemented"""

    @abstractmethod
    def search_classifiers(self, domain: SearchDomain) -> RecordsList:
        """Search classifiers method to be implemented"""

    @abstractmethod
    def search_schedules(self, domain: SearchDomain) -> RecordsList:
        """Search schedules method to be implemented"""

    @abstractmethod
    def search_slots(self, domain: SearchDomain) -> RecordsList:
        """Search slots method to be implemented"""


class StandardEstimarkInformer(EstimarkInformer):
    def __init__(self, task_repository: TaskRepository,
                 link_repository: LinkRepository,
                 classifier_repository: ClassifierRepository,
                 schedule_repository: ScheduleRepository,
                 slot_repository: SlotRepository) -> None:
        self.task_repository = task_repository
        self.link_repository = link_repository
        self.classifier_repository = classifier_repository
        self.schedule_repository = schedule_repository
        self.slot_repository = slot_repository

    def search_tasks(self, domain: SearchDomain) -> RecordsList:
        tasks = self.task_repository.search(domain)
        return [vars(task) for task in tasks]

    def search_links(self, domain: SearchDomain) -> RecordsList:
        links = self.link_repository.search(domain)
        return [vars(link) for link in links]

    def search_classifiers(self, domain: SearchDomain) -> RecordsList:
        classifiers = self.classifier_repository.search(domain)
        return [vars(classifier) for classifier in classifiers]

    def search_schedules(self, domain: SearchDomain) -> RecordsList:
        schedules = self.schedule_repository.search(domain)
        return [vars(schedule) for schedule in schedules]

    def search_slots(self, domain: SearchDomain) -> RecordsList:
        slots = self.slot_repository.search(domain)
        return [vars(slot) for slot in slots]
