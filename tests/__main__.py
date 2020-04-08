import sys, os

sys.path.append(os.path.abspath('./'))

from ising import *
import numpy as np

# Alias for np.random.rand
rand = np.random.rand

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

shape = (10, 10)

l = lattice(shape, all=1)
assert (l == 1).all()

l = lattice(shape, all=-1)
assert (l == -1).all()
