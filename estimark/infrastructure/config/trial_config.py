from .config import Config


class TrialConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = 'TEST'
        self['root'] = ''
        self['param'] = ''
        self['result'] = ''
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
            "ClassifierRepository": {
                "method": "memory_classifier_repository"
            },
            "ClassificationRepository": {
                "method": "memory_classification_repository"
            },
            "SlotRepository": {
                "method": "memory_slot_repository"
            },
            "ScheduleRepository": {
                "method": "memory_schedule_repository"
            },
            "EstimationCoordinator": {
                "method": "estimation_coordinator"
            },
            "EstimarkInformer": {
                "method": "standard_estimark_informer"
            }
        }
