"""
Authark entrypoint
"""

import os
import sys
import logging
from injectark import Injectark
from estimark.infrastructure.config import build_config
from estimark.infrastructure.factories import build_factory, build_strategy
from estimark.infrastructure.cli import Cli


def main(args):  # pragma: no cover
    config_path = os.environ.get('ESTIMARK_CONFIG', 'config.json')
    config = build_config('PROD', config_path)
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                        format='%(message)s')

    factory = build_factory(config)
    strategy = build_strategy(config['strategies'], config['strategy'])
    injector = Injectark(strategy=strategy, factory=factory)
    # injector['SetupSupplier'].setup()

    Cli(config, injector).run(args)


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
