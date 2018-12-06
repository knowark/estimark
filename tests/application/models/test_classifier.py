from estimark.application.models import Classifier


def test_classifier_instantiation():
    classifier = Classifier(id='XS', name='Extra Small', effort_id='TIME001')

    assert classifier.id == 'XS'
    assert classifier.name == 'Extra Small'
    assert classifier.effort_id == 'TIME001'
