from ising.metropolis import algorithm
import numpy as np


def test_algorithm():
    """
    Test metropolis algorithm
    """
    Ising = algorithm((50, 50))
