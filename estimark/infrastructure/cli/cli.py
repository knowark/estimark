import sys
from argparse import ArgumentParser, Namespace
from typing import Dict
from ..config import Config
from ..resolver import Registry


class Cli:
    def __init__(self, config: Config, registry: Registry) -> None:
        self.registry = registry
        self.config = config

    def run(self, args):
        namespace = self.parse(args)
        namespace.func(vars(namespace))

    def parse(self, args) -> Namespace:
        parser = ArgumentParser('Estimark')
        subparsers = parser.add_subparsers(dest='action')

        # Estimate
        estimate_parser = subparsers.add_parser('estimate')
        estimate_parser.set_defaults(func=self.estimate)

        # Show
        show_parser = subparsers.add_parser('show')
        show_parser.set_defaults(func=self.show)

        if len(args) == 0:
            parser.print_help()
            parser.exit()

        return parser.parse_args(args)

    def estimate(self, options_dict: Dict[str, str]) -> None:
        print('...ESTIMATE:::', options_dict)
        estimation_coordinator = self.registry['EstimationCoordinator']

    def show(self, options_dict: Dict[str, str]) -> None:
        print('...SHOW:::', options_dict)
        # estimark_informer = self.registry['EstimarkInformer']