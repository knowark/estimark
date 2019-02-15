from .trial_config import TrialConfig


class ProductionConfig(TrialConfig):
    def __init__(self):
        super().__init__()
        self['mode'] = 'PROD'
        self['root'] = ''
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
            }
        })
