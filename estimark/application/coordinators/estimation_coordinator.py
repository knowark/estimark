from typing import List, Dict, Any
from ..models import Schedule, Slot, Task
from ..repositories import (
    TaskRepository, ClassifierRepository, ClassificationRepository,
    LinkRepository, SlotRepository, ScheduleRepository)


class EstimationCoordinator:
    def __init__(self, task_repository: TaskRepository,
                 classifier_repository: ClassifierRepository,
                 classification_repository: ClassificationRepository,
                 link_repository: LinkRepository,
                 schedule_repository: ScheduleRepository,
                 slot_repository: SlotRepository
                 ) -> None:
        self.task_repository = task_repository
        self.classifier_repository = classifier_repository
        self.classification_repository = classification_repository
        self.link_repository = link_repository
        self.schedule_repository = schedule_repository
        self.slot_repository = slot_repository

    def estimate(self):
        slot_dict_list = self._calculate_slots()

        schedule = self.schedule_repository.add(
            Schedule(name='Project Schedule'))

        for slot_dict in slot_dict_list:
            slot_dict.update({'schedule_id': schedule.id})
            self.slot_repository.add(Slot(**slot_dict))

    def _calculate_slots(self) -> List[Dict[str, Any]]:
        effective_tasks = self.task_repository.search(
            [('summary', '=', False)])

        slots = []
        task_amounts_dict = {}
        for task in effective_tasks:
            task_amounts_dict[task.id] = self._calculate_amount(task.id)

        for task_id, amount in task_amounts_dict.items():
            predecessor_ids = self._calculate_predecessors(task_id)
            start = sum([task_amounts_dict.get(predecessor_id, 0)
                         for predecessor_id in predecessor_ids])
            end = start + amount
            slots.append({'task_id': task_id, 'start': start, 'end': end})

        return slots

    def _calculate_predecessors(self, task_id: str) -> List[str]:
        predecessor_ids = [
            predecessor.source for predecessor in
            self.link_repository.search([('target', '=', task_id)])]
        for predecessor_id in list(predecessor_ids):
            predecessor_ids.extend(
                self._calculate_predecessors(predecessor_id))
        return predecessor_ids

    def _calculate_amount(self, task_id: str) -> float:
        classifier_ids = [
            classification.classifier_id for classification in
            self.classification_repository.search(
                [('task_id', '=', task_id)])
        ]
        classifiers = self.classifier_repository.search(
            [('id', 'in', classifier_ids)])
        amount = sum([classifier.amount for classifier in classifiers])
        return amount
