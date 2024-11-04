import random

import numpy as np

from algorithms.configuration.configuration import Configuration
from simulator.services.debug import DebugLevel
from main import MainRunner
from analyzer.stat_runner import Runner
from utility.misc import flatten
from maps.map_manager import MapManager
from algorithms.algorithm_manager import AlgorithmManager


def main():
    random.seed(233423)
    np.random.seed(seed=233423)

    c: Configuration = Configuration()

    maps = MapManager.load_all(["House 3D"])
    maps = list(flatten(maps, depth=1))
    maps = dict(maps)
    c.maps = maps

    algos = AlgorithmManager.load_all(
        [
            "A*",
            "Wave-front",
            "Potential Field",
            "Dijkstra",
        ]
    )
    algos = list(flatten(algos, depth=1))
    algos = dict(algos)
    c.algorithms = algos

    # set configuration params
    c.simulator_write_debug_level = DebugLevel.LOW

    main_runner = MainRunner(c)
    runner = Runner(main_runner.main_services)
    runner.run_algorithms()


if __name__ == "__main__":
    main()
