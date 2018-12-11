from .config import Config


class TrialConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = 'TEST'
        self['factory'] = 'TrialFactory'
        self['providers'] = {
            "ExpressionParser": {
                "method": "expression_parser"
            },
            "TaskRepository": {
                "method": "memory_task_repository"
            },
            "EstimationCoordinator": {
                "method": "estimation_coordinator"
            },
            "EstimarkInformer": {
                "method": "standard_estimark_informer"
            }
        }
