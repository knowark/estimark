
def test_initialization_manager_instantiation(initialization_manager):
    assert initialization_manager is not None


def test_initialization_manager_initialize_non_empty(initialization_manager):
    initialization_manager.initialize()

    classifiers = initialization_manager.classifier_repository.data['data']

    assert len(classifiers) == 5


def test_initialization_manager_initialize_empty(initialization_manager):
    initialization_manager.classifier_repository.data['data'] = {}
    classifiers = initialization_manager.classifier_repository.data['data']

    assert len(classifiers) == 0

    initialization_manager.initialize()
    classifiers = initialization_manager.classifier_repository.data['data']

    assert len(classifiers) == 9
