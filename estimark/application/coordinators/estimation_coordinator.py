from ..models import Schedule
from ..repositories import TaskRepository


class EstimationCoordinator:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def estimate(self):
        return vars(Schedule())
