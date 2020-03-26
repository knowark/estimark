import multiprocessing
from typing import Dict, Any
from abc import ABC, abstractmethod
from json import loads, JSONDecodeError
from pathlib import Path


class Config(dict, ABC):
    @abstractmethod
    def __init__(self):
        self['mode'] = 'BASE'
        self['strategy'] = {}
        self['strategies'] = ['base']


class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = 'DEV'
        self['factory'] = 'CheckFactory'
        self['root'] = ''
        self['param'] = ''
        self['result'] = ''
        self['strategies'].extend(['check'])


class ProductionConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = 'PROD'
        self['root'] = ''
        self['param'] = ''
        self['result'] = ''
        self['factory'] = 'RstFactory'
        self['strategies'].extend(['rst'])
