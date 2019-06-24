from typing import List, Dict, Any
from ..models import Schedule, Slot, Task
from ..repositories import (
    TaskRepository, ClassifierRepository, ClassificationRepository,
    LinkRepository, SlotRepository, ScheduleRepository)
from ..services import PlotService


class EstimationCoordinator:
    def __init__(self, task_repository: TaskRepository,
                 classifier_repository: ClassifierRepository,
                 classification_repository: ClassificationRepository,
                 link_repository: LinkRepository,
                 schedule_repository: ScheduleRepository,
                 slot_repository: SlotRepository,
                 plot_service: PlotService
                 ) -> None:
        self.task_repository = task_repository
        self.classifier_repository = classifier_repository
        self.classification_repository = classification_repository
        self.link_repository = link_repository
        self.schedule_repository = schedule_repository
        self.slot_repository = slot_repository
        self.plot_service = plot_service

    def estimate(self, state=None):
        slot_dict_list = self._calculate_slots(state)

        schedule = self.schedule_repository.add(
            Schedule(name='Project Schedule'))

        for slot_dict in slot_dict_list:
            slot_dict.update({'schedule_id': schedule.id})
            self.slot_repository.add(Slot(**slot_dict))

    def plot(self, schedule_id: str = None) -> bool:
        schedule = None
        if schedule_id:
            schedule = self.schedule_repository.get(schedule_id)
        else:
            schedules = self.schedule_repository.search([])
            schedule = schedules[-1] if schedules else None
        if not schedule:
            return False

        self.plot_service.plot(schedule)
        return True

    def _calculate_slots(self, state=None) -> List[Dict[str, Any]]:
        domain = [('summary', '=', False)]
        if state:
            domain.append(('state', '=', state))
        effective_tasks = self.task_repository.search(domain)

        slots = []
        task_amounts_dict = {}
        for task in effective_tasks:
            task_amounts_dict[task.id] = {
                'name': task.name,
                'amount':  self._calculate_amount(task.id)
            }

        for task_id, values in task_amounts_dict.items():
            start = self._calculate_start(task_amounts_dict, task_id)
            end = start + values['amount']
            slots.append({'name': values['name'], 'task_id': task_id,
                          'start': start, 'end': end})

        return slots

    def _calculate_start(self, task_amounts_dict, task_id):
        durations = [0]
        predecessor_ids = [
            predecessor.source for predecessor in
            self.link_repository.search([('target', '=', task_id)])]
        for predecessor_id in predecessor_ids:
            duration = self._calculate_start(task_amounts_dict, predecessor_id)
            duration += task_amounts_dict.get(
                predecessor_id, {}).get('amount', 0)
            durations.append(duration)
        return max(durations)

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
