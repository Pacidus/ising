from ising import lattice
import numpy as np

# Alias for np.random.rand
rand = np.random.rand


def test_2Drandinit():
    """
    2D test randomize state initialisation
    """
    for i in range(100):
        a = int(1 + rand() * 1000)
        b = int(1 + rand() * 1000)
        r = rand()

        l = lattice((a, b), r=r)

        shape = l.shape
        size = l.size
        val = (l == 1).sum()

        assert size == a * b
        assert shape == (a, b)
        assert val == int(r * size)


def test_2Dall():
    """
    2D test all state initialisation
    """

    shape = (10, 10)

    l = lattice(shape, all=1)
    assert (l == 1).all()

    l = lattice(shape, all=-1)
    assert (l == -1).all()


def test_RanDimShape():
    """
    Test 1D to 4D randomize and all ratio initialisation
    with random shape
    """

    for d in range(1, 5):
        for i in range(100):
            shape = tuple()
            for j in range(d):
                shape += (int(1 + rand() * 100),)

        r = rand()

        l = lattice(shape, r=r)

        val = (l == 1).sum()

        size = 1
        for i in shape:
            size *= i
        assert l.size == size
        assert l.shape == shape
        assert val == int(r * l.size)

        l = lattice(shape, all=1)
        assert (l == 1).all()

        l = lattice(shape, all=-1)
        assert (l == -1).all()


def test_H():
    """
    Test the Hamiltonian for 2D lattices
    """

    for i in range(50):
        l = lattice((100 + i, 100 + i))
        H = l.mH()
        assert H ** 2 < 1  # can be false but it's improbable

        l = lattice((100 + i, 100 + i), all=1)
        H = l.mH()
        assert H == -4

        l = lattice((100 + i, 100 + i), all=-1)
        H = l.mH()
        assert H == -4
