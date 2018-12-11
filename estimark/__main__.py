"""
Authark entrypoint
"""

import os
from .infrastructure.config import build_config
from .infrastructure.factories import build_factories
from .infrastructure.resolver import Resolver
from .infrastructure.cli import Cli


def main():  # pragma: no cover
    mode = os.environ.get('ESTIMARK_MODE', 'PROD')
    config_path = os.environ.get('ESTIMARK_CONFIG', 'estimark_config.json')
    config = build_config(config_path, mode)

    factories = build_factories(config)
    resolver = Resolver(config, factories)
    providers = config['providers']
    registry = resolver.resolve(providers)

    Cli(config, registry).run()


if __name__ == '__main__':  # pragma: no cover
    main()
