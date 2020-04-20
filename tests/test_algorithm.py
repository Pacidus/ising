from isingm.metropolis import algorithm
import numpy as np


def test_algorithm():
    """
    Test metropolis algorithm
    """

    Ising = algorithm((100, 100))

    for i in range(10):
        E0 = Ising.mH()

        for j in range(30):
            Ising.step(100)

        E1 = Ising.mH()

        assert E0 >= E1  # Can fail
