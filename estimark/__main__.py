"""
Authark entrypoint
"""

import os
import sys
from .infrastructure.config import build_config
from .infrastructure.factories import build_factories
from .infrastructure.resolver import Resolver
from .infrastructure.cli import Cli


def main(args):  # pragma: no cover
    mode = os.environ.get('ESTIMARK_MODE', 'PROD')
    config_path = os.environ.get('ESTIMARK_CONFIG', 'estimark_config.json')
    config = build_config(config_path, mode)

    factories = build_factories(config)
    resolver = Resolver(config, factories)
    providers = config['providers']
    registry = resolver.resolve(providers)

    Cli(config, registry).run(args)


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
