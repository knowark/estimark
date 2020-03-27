import json
import logging
from typing import Dict
from abc import ABC, abstractmethod
from ..models import Schedule, Slot
from ..repositories import SlotRepository


logger = logging.getLogger(__name__)


class PlotService(ABC):
    @abstractmethod
    def plot(self, schedule: Schedule) -> str:
        "Plot method to be implemented."


class MemoryPlotService(PlotService):
    def __init__(self, slot_repository: SlotRepository) -> None:
        self.slot_repository = slot_repository

    def plot(self, schedule: Schedule) -> None:
        logging.info(f"MEMORY PLOT. SCHEDULE: {schedule.name}")
