import sys
from json import dumps
from argparse import ArgumentParser, Namespace
from typing import Dict
from injectark import Injectark
from ... import __version__
from ..config import Config


class Cli:
    def __init__(self, config: Config, resolver: Injectark) -> None:
        self.resolver = resolver
        self.config = config

    def run(self, args):
        namespace = self.parse(args)
        namespace.func(vars(namespace))

    def parse(self, args) -> Namespace:
        parser = ArgumentParser('Estimark')
        subparsers = parser.add_subparsers(dest='action')

        # Estimate
        estimate_parser = subparsers.add_parser('estimate')
        estimate_parser.add_argument('-s', '--state')
        estimate_parser.set_defaults(func=self.estimate)

        # Show
        show_parser = subparsers.add_parser('show')
        show_parser.add_argument('-t', '--tasks', action='store_true')
        show_parser.add_argument('-l', '--links', action='store_true')
        show_parser.add_argument('-c', '--classifiers', action='store_true')
        show_parser.add_argument('-s', '--schedules', action='store_true')
        show_parser.add_argument('-o', '--slots', action='store_true')
        show_parser.set_defaults(func=self.show)

        # Plot
        plot_parser = subparsers.add_parser('plot')
        plot_parser.set_defaults(func=self.plot)

        # Version
        version_parser = subparsers.add_parser('version')
        version_parser.set_defaults(func=self.version)

        if len(args) == 0:
            parser.print_help()
            parser.exit()

        return parser.parse_args(args)

    def estimate(self, options_dict: Dict[str, str]) -> None:
        print('...ESTIMATE:::', options_dict)

        state = options_dict.get('state')
        estimation_coordinator = self.resolver['EstimationCoordinator']
        estimation_coordinator.estimate(state)

    def show(self, options_dict: Dict[str, str]) -> None:
        print('...SHOW:::', options_dict)
        estimark_informer = self.resolver['EstimarkInformer']

        if options_dict.get('tasks'):
            tasks = estimark_informer.search_tasks([])
            for task in tasks:
                print('T:::', task)
        elif options_dict.get('links'):
            links = estimark_informer.search_links([])
            for link in links:
                print('L:::', link)
        elif options_dict.get('classifiers'):
            classifiers = estimark_informer.search_classifiers([])
            for classifier in classifiers:
                print('C:::', classifier)
        elif options_dict.get('schedules'):
            schedules = estimark_informer.search_schedules([])
            for schedule in schedules:
                print('S:::', schedule)
        elif options_dict.get('slots'):
            slots = estimark_informer.search_slots([])
            for slot in slots:
                print('S:::', slot)

    def plot(self, options_dict: Dict[str, str]):
        print('CLI PLOT |||||')
        estimation_coordinator = self.resolver['EstimationCoordinator']
        estimation_coordinator.plot()

    def version(self, options_dict: Dict[str, str]):
        print('VERSION:')
        print(__version__)
