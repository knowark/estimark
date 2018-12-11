import sys
from argparse import ArgumentParser, Namespace
from ..config import Config
from ..resolver import Registry


class Cli:
    def __init__(self, config: Config, registry: Registry) -> None:
        self.registry = registry
        self.config = config

    def run(self):
        args = self.parse()
        args.func(args)

    def parse(self) -> Namespace:
        parser = ArgumentParser('Estimark')
        subparsers = parser.add_subparsers()

        # Estimate
        estimate_parser = subparsers.add_parser('estimate')
        estimate_parser.set_defaults(func=self.estimate)

        # Show
        show_parser = subparsers.add_parser('show')
        show_parser.set_defaults(func=self.show)

        if len(sys.argv[1:]) == 0:
            parser.print_help()
            parser.exit()

        return parser.parse_args()

    def estimate(self, args: Namespace) -> None:
        print('...ESTIMATE:::', args)
        estimation_coordinator = self.registry['estimation_coordinator']

    def show(self, args: Namespace) -> None:
        print('...SHOW:::', args)
        estimark_informer = self.registry['estimark_informer']
