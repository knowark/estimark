import os
from typing import Dict, Any


Config = Dict[str, Any]


config: Config = {
    "factory": os.environ.get('ESTIMARK_FACTORY', 'RstFactory'),
    "strategies": os.environ.get(
        'ESTIMARK_STRATEGIES', 'base,altair,json,rst').split(','),
    "root_dir": os.environ.get('ESTIMARK_ROOT_DIR', ''),
    "param_dir": os.environ.get('ESTIMARK_PARAM_DIR', ''),
    "result_dir": os.environ.get('ESTIMARK_RESULT_DIR', ''),
    "plot_dir": os.environ.get('ESTIMARK_PLOT_DIR', ''),
}
