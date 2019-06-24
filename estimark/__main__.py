"""
Authark entrypoint
"""

import os
import sys
from injectark import Injectark
from estimark.infrastructure.config import build_config
from estimark.infrastructure.factories import build_factory
from estimark.infrastructure.cli import Cli


def main(args):  # pragma: no cover
    mode = os.environ.get('ESTIMARK_MODE', 'PROD')
    config_path = os.environ.get('ESTIMARK_CONFIG', 'config.json')
    config = build_config(config_path, mode)

    factory = build_factory(config)
    strategy = config['strategy']
    resolver = Injectark(strategy=strategy, factory=factory)

    Cli(config, resolver).run(args)


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
