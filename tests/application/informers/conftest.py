from pytest import fixture


@fixture
def estimark_informer(trial_resolver):
    return trial_resolver.resolve('EstimarkInformer')
