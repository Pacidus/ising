from ising.metropolis import algorithm
import numpy as np


def test_algorithm():
    """
    Test metropolis algorithm
    """
    Ising = algorithm((10, 10))

    for i in range(10):
        E0 = Ising.mH()

        for j in range(30):
            Ising.step(10)

        E1 = Ising.mH()

        assert E0 >= E1
