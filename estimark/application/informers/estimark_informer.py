from abc import ABC, abstractmethod
from ..repositories import TaskRepository, LinkRepository
from .types import SearchDomain, RecordsList


class EstimarkInformer(ABC):

    @abstractmethod
    def search_tasks(self, domain: SearchDomain) -> RecordsList:
        """Search tasks method to be implemented"""

    @abstractmethod
    def search_links(self, domain: SearchDomain) -> RecordsList:
        """Search links method to be implemented"""


class StandardEstimarkInformer(EstimarkInformer):
    def __init__(self, task_repository: TaskRepository,
                 link_repository: LinkRepository) -> None:
        self.task_repository = task_repository
        self.link_repository = link_repository

    def search_tasks(self, domain: SearchDomain) -> RecordsList:
        tasks = self.task_repository.search(domain)
        return [vars(task) for task in tasks]

    def search_links(self, domain: SearchDomain) -> RecordsList:
        links = self.link_repository.search(domain)
        return [vars(link) for link in links]
