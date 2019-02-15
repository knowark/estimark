from typing import Dict
from pytest import fixture, raises
from estimark.application.models import Link
from estimark.application.repositories import ExpressionParser
from estimark.infrastructure.data import RstLoader
from estimark.infrastructure.data import RstLinkRepository


@fixture
def rst_link_repository(rst_loader) -> RstLinkRepository:
    parser = ExpressionParser()
    repository = RstLinkRepository(parser, rst_loader)
    return repository


def test_rst_link_repository_instantiation(rst_link_repository) -> None:
    assert rst_link_repository is not None
    assert rst_link_repository.item_class is Link


def test_rst_link_repository_load(rst_link_repository) -> None:
    rst_link_repository.load()
    assert len(rst_link_repository.items) > 0


def test_rst_link_repository_search(rst_link_repository) -> None:
    rst_link_repository.load()
    links = rst_link_repository.search([('target', '=', '2.2.2')])
    assert len(links) == 1
    for link in links:
        assert link.source == '2.2.1'
        assert link.target == '2.2.2'


def test_rst_link_repository_search_with_predecessors(
        rst_link_repository) -> None:
    rst_link_repository.load()
    links = rst_link_repository.search([('target', '=', '2.1.2.3')])
    assert len(links) == 2
    assert links[0].source == '2.1.2.1'
    assert links[0].target == '2.1.2.3'
    assert links[1].source == '1.1.2'
    assert links[1].target == '2.1.2.3'
