from estimark.application.informers import EstimarkInformer


def test_estimark_informer_instantiation(estimark_informer):
    assert estimark_informer is not None


def test_estimark_informer_search_tasks(estimark_informer):
    result = estimark_informer.search_tasks([])

    assert len(result) == 3


def test_estimark_informer_search_links(estimark_informer):
    result = estimark_informer.search_links([])

    assert len(result) == 0


def test_estimark_informer_search_classifiers(estimark_informer):
    result = estimark_informer.search_classifiers([])

    assert len(result) == 0


def test_estimark_informer_search_schedules(estimark_informer):
    result = estimark_informer.search_schedules([])

    assert len(result) == 0


def test_estimark_informer_search_slots(estimark_informer):
    result = estimark_informer.search_slots([])

    assert len(result) == 0
