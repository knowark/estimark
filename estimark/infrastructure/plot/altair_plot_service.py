
import altair as alt
import pandas as pd
import logging
from typing import List
from datetime import date
from pathlib import Path
from collections import Counter
from ...application.models import Schedule, Task
from ...application.repositories import SlotRepository
from ...application.services import PlotService


logger = logging.getLogger(__name__)


class AltairPlotService(PlotService):
    def __init__(self, plot_dir: str,
                 slot_repository: SlotRepository) -> None:
        self.slot_repository = slot_repository
        self.plot_dir = plot_dir
        self.output_file = str(Path(plot_dir).joinpath('chart.html'))

    def plot_gantt(self, schedule: Schedule) -> None:
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
        ).properties(title=title)

        chart.save(self.output_file)

    def plot_kanban(self, tasks: List[Task]) -> None:
        logging.info(f"ALTAIR KANBAN PLOT. TASKS #: {len(tasks)}")

        task_dict_list = [{'weight': 1, **vars(task)}
                          for task in tasks if not task.summary]

        state_counts = Counter(task_dict['state'] for task_dict
                               in task_dict_list).most_common()
        _, max_depth = next(iter(state_counts))

        source = pd.DataFrame(task_dict_list)

        title = f"Kanban Chart | {date.today()}"
        block_height = 50
        block_width = block_height * 5

        base = alt.Chart(source).mark_bar(
            color='black'
        ).encode(
            x=alt.X('state', axis=alt.Axis(orient='top', labelAngle=0,
                                           labelFontSize=15)),
            y=alt.Y('sum(weight)', sort='descending', stack='zero'),
            order=alt.Order('id',  sort='ascending')
        ).properties(
            title=title,
            width=block_width * len(state_counts),
            height=block_height * max_depth)

        bars = base.encode(
            color='id')

        text = base.mark_text(
            dy=-(block_height / 2),
            color='black'
        ).encode(
            text='name')

        chart = bars + text

        self.output_file = str(Path(self.plot_dir).joinpath('kanban.html'))

        chart.save(self.output_file)
