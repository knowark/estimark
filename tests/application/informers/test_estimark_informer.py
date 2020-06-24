

def test_estimark_informer_instantiation(estimark_informer):
    assert estimark_informer is not None


def test_estimark_informer_search_tasks(estimark_informer):
    result = estimark_informer.search('task', [])

    assert len(result) == 3


def test_estimark_informer_search_links(estimark_informer):
    result = estimark_informer.search('link', [])

    assert len(result) == 0


def test_estimark_informer_search_classifiers(estimark_informer):
    result = estimark_informer.search('classifier', [])

    assert len(result) == 0


def test_estimark_informer_search_schedules(estimark_informer):
    result = estimark_informer.search('schedule', [])

    assert len(result) == 0


def test_estimark_informer_search_slots(estimark_informer):
    result = estimark_informer.search('slot', [])

    assert len(result) == 0
