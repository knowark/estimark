from estimark.infrastructure.data import RstAnalyzer


def test_rst_analyzer_definition(rst_analyzer) -> None:
    assert rst_analyzer is not None


def test_rst_analyzer_analyzes_rst_file(rst_analyzer, rst_file):
    result = rst_analyzer.analyze(rst_file)

    assert result is not None
    assert result == {'classifiers': 'XS', 'role': 'PM'}
