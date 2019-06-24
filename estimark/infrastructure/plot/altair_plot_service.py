
import altair as alt
import pandas as pd
from datetime import date
from pathlib import Path
from ...application.models import Schedule
from ...application.repositories import SlotRepository
from ...application.services import PlotService


class AltairPlotService(PlotService):
    def __init__(self, plot_dir: str,
                 slot_repository: SlotRepository) -> None:
        self.plot_dir = plot_dir
        self.slot_repository = slot_repository

    def plot(self, schedule: Schedule) -> None:
        print("::::ALTAIR PLOT SCHEDULE: {}::::".format(schedule.name))
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

        output_file = str(Path(self.plot_dir).joinpath('chart.html'))
        chart.save(output_file)