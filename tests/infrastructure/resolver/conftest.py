from pytest import fixture
from estimark.infrastructure.resolver import Resolver, Config


class ParHelper:
    pass


class MemoryParHelper(ParHelper):
    pass


class FooRepository:
    pass


class MemoryFooRepository(FooRepository):
    def __init__(self, par_helper: ParHelper) -> None:
        pass


class BarRepository:
    pass


class MemoryBarRepository(BarRepository):
    def __init__(self, par_helper: ParHelper) -> None:
        pass


class StandardBazService:
    def __init__(self, foo_repository: FooRepository,
                 bar_repository: BarRepository) -> None:
        self.foo_repository = foo_repository
        self.bar_repository = bar_repository


@fixture
def config():
    config = {
        'factory': 'MockFactory'
    }
    return config


@fixture
def mock_factory():
    class MockFactory:

        def memory_par_helper(self):
            return MemoryParHelper()

        def memory_foo_repository(self, par_helper: ParHelper):
            return MemoryFooRepository(par_helper)

        def memory_bar_repository(self, par_helper: ParHelper):
            return MemoryBarRepository(par_helper)

        def standard_baz_service(self, foo_repository: FooRepository,
                                 bar_repository: BarRepository):
            return StandardBazService(foo_repository, bar_repository)

        def dedicated_foo_repository(self, par_helper: ParHelper):
            return MemoryFooRepository(par_helper)

    return MockFactory()


@fixture
def providers_dict():
    return {
        "FooRepository": {
            "method": "memory_foo_repository"
        },
        "BarRepository": {
            "method": "memory_bar_repository"
        },
        "BazService": {
            "method": "standard_baz_service"
        },
        "ParHelper": {
            "method": "memory_par_helper"
        }
    }


@fixture
def dedicated_providers_dict():
    return {
        "FooRepository": {
            "method": "memory_foo_repository"
        },
        "BarRepository": {
            "method": "memory_bar_repository"
        },
        "BazService": {
            "method": "standard_baz_service",
            "providers": {
                "FooRepository": "dedicated_foo_repository"
            }
        },
        "ParHelper": {
            "method": "memory_par_helper"
        },
    }


@fixture
def factories(mock_factory):
    return {
        'MockFactory': mock_factory
    }


@fixture
def resolver(config, factories):
    resolver = Resolver(config, factories)
    return resolver
