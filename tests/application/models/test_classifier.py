from estimark.application.models import Classifier


def test_classifier_instantiation():
    classifier = Classifier(id='XS', name='Extra Small', amount=5)

    assert classifier.id == 'XS'
    assert classifier.name == 'Extra Small'
    assert classifier.amount == 5
    assert classifier.units == 'days'
