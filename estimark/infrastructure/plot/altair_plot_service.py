
import altair as alt
import pandas as pd
import logging
from typing import List
from datetime import date
from pathlib import Path
from ...application.models import Schedule, Task
from ...application.repositories import SlotRepository
from ...application.services import PlotService


logger = logging.getLogger(__name__)


class AltairPlotService(PlotService):
    def __init__(self, plot_dir: str,
                 slot_repository: SlotRepository) -> None:
        self.slot_repository = slot_repository
        self.output_file = str(Path(plot_dir).joinpath('chart.html'))

    def plot(self, schedule: Schedule) -> None:
        logging.info(f"ALTAIR PLOT SCHEDULE: {schedule.name}")
        slots = self.slot_repository.search(
            [('schedule_id', '=', schedule.id)])
        slot_dict_list = [vars(slot) for slot in slots]
        state = f"| State: <{schedule.state}> " if schedule.state else ""
        title = f"{schedule.name} {state}| {date.today()}"

        source = pd.DataFrame(slot_dict_list)
        chart = alt.Chart(source).mark_bar().encode(
            x='start',
            x2='end',
            y='name'
        ).properties(
            title=title)

        chart.save(self.output_file)

    def plot_kanban(self, tasks: List[Task]) -> None:
        logging.info(f"ALTAIR KANBAN PLOT. TASKS #: {len(tasks)}")
        # slots = self.slot_repository.search(
        #     [('schedule_id', '=', schedule.id)])
        # slot_dict_list = [vars(slot) for slot in slots]
        # state = f"| State: <{schedule.state}> " if schedule.state else ""
        # title = f"{schedule.name} {state}| {date.today()}"

        # source = pd.DataFrame(slot_dict_list)
        # chart = alt.Chart(source).mark_bar().encode(
        #     x='start',
        #     x2='end',
        #     y='name'
        # ).properties(
        #     title=title)

        # chart.save(self.output_file)
