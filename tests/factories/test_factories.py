import inspect
from injectark import Injectark
from estimark.core.common import config
from estimark.factories import factory_builder


test_tuples = [
    ('BaseFactory', [
        ('QueryParser', 'QueryParser'),
        ('TaskRepository', 'MemoryTaskRepository'),
        ('LinkRepository', 'MemoryLinkRepository'),
        ('ClassifierRepository', 'MemoryClassifierRepository'),
        ('ClassificationRepository', 'MemoryClassificationRepository'),
        ('ScheduleRepository', 'MemoryScheduleRepository'),
        ('SlotRepository', 'MemorySlotRepository'),
        ('PlotService', 'MemoryPlotService'),
        ('EstimationManager', 'EstimationManager'),
        ('InitializationManager', 'InitializationManager'),
        ('EstimarkInformer', 'StandardEstimarkInformer')
    ]),
    ('AltairFactory', [
        ('PlotService', 'AltairPlotService')
    ]),
    ('CheckFactory', [
        ('TaskRepository', 'MemoryTaskRepository')
    ]),
    ('JsonFactory', [
        ('TaskRepository', 'JsonTaskRepository'),
        ('LinkRepository', 'JsonLinkRepository'),
        ('ClassifierRepository', 'JsonClassifierRepository'),
        ('ClassificationRepository', 'JsonClassificationRepository'),
        ('ScheduleRepository', 'JsonScheduleRepository'),
        ('SlotRepository', 'JsonSlotRepository')
    ]),
    ('RstFactory', [
        ('RstAnalyzer', 'RstAnalyzer'),
        ('RstLoader', 'RstLoader'),
        ('TaskRepository', 'RstTaskRepository'),
        ('LinkRepository', 'RstLinkRepository'),
        ('ClassificationRepository', 'RstClassificationRepository'),
    ]),
]


def test_factories():
    for factory_name, dependencies in test_tuples:
        factory = factory_builder.build(config, name=factory_name)

        injector = Injectark(factory=factory)

        for abstract, concrete in dependencies:
            result = injector.resolve(abstract)
            assert type(result).__name__ == concrete
