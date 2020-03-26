from ..config import Config
from ...application.repositories import SlotRepository
from ..plot import AltairPlotService
from .memory_factory import MemoryFactory


class AltairFactory(MemoryFactory):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config
        self.plot_dir = self.config.get('plot_dir', '.')

    def altair_plot_service(self, slot_repository: SlotRepository,
                            ) -> AltairPlotService:
        plot_service = AltairPlotService(
            self.plot_dir, slot_repository)
        return plot_service
