from .trial_config import TrialConfig


class ProductionConfig(TrialConfig):
    def __init__(self):
        super().__init__()
        self['mode'] = 'PROD'
        self['root'] = ''
        self['param'] = ''
        self['result'] = ''
        self['factory'] = 'RstFactory'
        self['strategy'].update({
            "RstAnalyzer": {
                "method": "rst_analyzer"
            },
            "RstLoader": {
                "method": "rst_loader"
            },
            "TaskRepository": {
                "method": "rst_task_repository"
            },
            "LinkRepository": {
                "method": "rst_link_repository"
            },
            "ClassifierRepository": {
                "method": "json_classifier_repository"
            },
            "ClassificationRepository": {
                "method": "rst_classification_repository"
            },
            "SlotRepository": {
                "method": "json_slot_repository"
            },
            "PlotService": {
                "method": "altair_plot_service"
            },
            "ScheduleRepository": {
                "method": "json_schedule_repository"
            }
        })
