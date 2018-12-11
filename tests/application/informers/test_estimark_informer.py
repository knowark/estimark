from estimark.application.informers import EstimarkInformer


def test_estimark_informer_instantiation(estimark_informer):
    assert estimark_informer is not None


def test_estimark_informer_search_tasks(estimark_informer):
    result = estimark_informer.search_tasks([])

    assert len(result) == 3
