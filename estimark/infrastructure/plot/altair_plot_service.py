from ...application.repositories import SlotRepository


class AltairPlotService():
    def __init__(self, plot_dir: str,
                 slot_repository: SlotRepository) -> None:
        self.plot_dir = plot_dir
        self.slot_repository = slot_repository
