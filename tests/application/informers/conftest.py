from pytest import fixture


@fixture
def estimark_informer(trial_registry):
    return trial_registry['EstimarkInformer']
