from ising import lattice
import numpy as np
import pytest

# Alias for np.random.rand
rand = np.random.rand
dM = 7
dim = range(1, dM)
m = 1
M = 10000
t = 10
size = np.linspace(m, M, t).astype(int)
tests = range(100)


def unit_test(shape, ratio):
    """
    Unit test for lattice
    """
    Ising = lattice(shape, r=ratio)

    Shape = Ising.__shape__
    size = Ising.__size__
    val = (Ising == 1).sum()
    D = len(shape)

    del Ising

    Size = 1
    for i in shape:
        Size *= i

    assert size == Size
    assert shape == Shape
    assert val == int(ratio * size)

    Ising = lattice(shape, all=1)
    assert (Ising == 1).all()
    H = Ising.mH()
    assert H == -2 * D
    del Ising

    Ising = lattice(shape, all=-1)
    assert (Ising == -1).all()
    H = Ising.mH()
    assert H == -2 * D
    del Ising


@pytest.mark.parametrize("d", dim)
def test_args(d):
    """
    Test the initialisation for 1D to 6D
    """
    D = range(d - 1)
    for s in size:
        for test in tests:
            S = s
            shape = tuple()

            V = 1
            for j in D:
                v = 1 + int(rand() * np.sqrt(S))
                S = 1 + int(S / v)
                shape = shape + (v,)
                V *= v

            shape = shape + (int(S),)
            V *= int(S)

            unit_test(shape, rand())
