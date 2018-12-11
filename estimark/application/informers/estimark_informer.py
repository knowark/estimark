from abc import ABC, abstractmethod
from ..repositories import TaskRepository
from .types import SearchDomain, RecordsList


class EstimarkInformer(ABC):

    @abstractmethod
    def search_tasks(self, domain: SearchDomain) -> RecordsList:
        """Search tasks method to be implemented"""


class StandardEstimarkInformer(EstimarkInformer):
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def search_tasks(self, domain: SearchDomain) -> RecordsList:
        tasks = self.task_repository.search(domain)
        return [vars(task) for task in tasks]
