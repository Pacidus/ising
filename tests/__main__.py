import sys, os

sys.path.append(os.path.abspath('./'))

from ising import *
import numpy as np

# Alias for np.random.rand
rand = np.random.rand

"""
 2D randomize ratio respect
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


"""
 2D all ratio respect
"""

shape = (10, 10)

l = lattice(shape, all=1)
assert (l == 1).all()

l = lattice(shape, all=-1)
assert (l == -1).all()


"""
1D to 4D randomize and all ratio respect
"""

for d in range(1,5):
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

