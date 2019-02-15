from .config import Config


class TrialConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = 'TEST'
        self['factory'] = 'TrialFactory'
        self['strategy'] = {
            "ExpressionParser": {
                "method": "expression_parser"
            },
            "TaskRepository": {
                "method": "memory_task_repository"
            },
            "LinkRepository": {
                "method": "memory_link_repository"
            },
            "EstimationCoordinator": {
                "method": "estimation_coordinator"
            },
            "EstimarkInformer": {
                "method": "standard_estimark_informer"
            }
        }
