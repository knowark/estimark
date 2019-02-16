import json
from typing import Dict
from abc import ABC, abstractmethod
from ..models import Schedule, Slot
from ..repositories import SlotRepository


class PlotService(ABC):
    @abstractmethod
    def plot(self, schedule: Schedule) -> str:
        "Plot method to be implemented."


class MemoryPlotService(PlotService):
    def __init__(self, slot_repository: SlotRepository) -> None:
        self.slot_repository = slot_repository

    def plot(self, schedule: Schedule) -> None:
        print("::::SERVICE PLOT SCHEDULE: {}::::".format(schedule.name))
        slots = self.slot_repository.search(
            [('schedule_id', '=', schedule.id)])
        for slot in slots:
            print('||==', vars(slot))
