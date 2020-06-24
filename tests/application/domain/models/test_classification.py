from estimark.application.domain.models import Classification


def test_classification_instantiation():
    classification = Classification(id='1', classifier_id='XS',
                                    task_id='T001')

    assert classification.id == '1'
    assert classification.classifier_id == 'XS'
    assert classification.task_id == 'T001'
