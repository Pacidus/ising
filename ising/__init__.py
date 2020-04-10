# coding:utf-8

"""
@author: Pacidus

A module for the Ising model
"""

__version__ = "0.1.0"

import numpy as np

# Alias for np.random.rand
__randm__ = np.random.rand
# Alias for np.random.randint
__randint__ = np.random.randint


class lattice:
    """
    It's the main place of the ising model,
    we have to initialize it with a tuple of the shape of the lattice wich can be any dimension or size.
    The lattice can by initialized with a randomized state (you can choose the ratio of up state) or all in 1 or -1 state.

    ### arguments:

    - ##### shape:
    >   type: tuple of int
    >
    >
    >   the shape of the lattice is tested for 1 to 4 dimension

    ##### Optionnal:

    - ##### all: 

    >    type: **int** == 1 or -1
    >
    >    set the state at all 1 or -1 it overpass the r parrameter

    - ##### r: 

    >   type: **float** in [0, 1]
    >
    >   set a random state with a ratio r of 1 in the lattice (default r = 0.5)

    - ##### adj: 

    >   type: **numpy.array**
    >
    >   a vector of vector: is the representation of the spin interaction
    >
    >   |  0  |  J  |  0  |
    >   | --- | --- | --- |
    >   |**J**|**#**|**J**| 
    >   |**0**|**J**|**0**| 
    >
    >   will be written as [[1,0],[-1,0],[0,1],[0,-1]]
    >   
    >   (as default it's the left right up down direct neighbor matrix will be genereted (whatever this mean in 4 or more dimensions))

    - ##### J:

    >   type: **numpy.array** or **float**
    >
    >   Is the interraction between spins, 
    >   if J is an array he as to be the same length than adj 
    >
    >   (you can choose to make anisotropic iteractions !!)

    - ##### B:
    >   type **numpy.array** or **float**
    >   is the magnetic field imposed on the lattice
    >   if B is an array he as to have the same shape of the lattice 

    """

    def __init__(self, shape, *args, **kwargs):
        self.__shape__ = shape
        self.__lattice__ = np.empty(shape)

        self.shape = self.__shape__
        self.dim = len(shape)

        self.size = 1
        for i in range(self.dim):
            self.size *= self.shape[i]

        if "all" in kwargs:
            self.all(kwargs["all"])
        elif "r" in kwargs:
            self.randomize(kwargs["r"])
        else:
            self.randomize()

        if "adj" in kwargs:
            self.adj = kwargs["adj"]
        else:
            adj = []
            for i in range(2):
                for j in range(self.dim):
                    vec = [0] * self.dim
                    vec[j] = i * 2 - 1
                    adj.append(vec)

            self.adj = np.array(adj)

        self.J = np.ones(self.adj.shape[0])
        if "J" in kwargs:
            self.J *= kwargs["J"]

        self.B = np.zeros(shape)
        if "B" in kwargs:
            self.B += kwargs["B"]

    def __eq__(self, value):
        return self.__lattice__ == value

    def __sum_adj__(self):
        """
        Sum the adjacents contribution of the hamiltionian
        """

        J = self.J  # The interaction
        adj = self.adj  # The vector of the adjacent

        n, d = adj.shape  # n: number of adjacent, d: the dimension

        dim = range(d)
        neigh = range(n)

        Sum = np.zeros(self.__shape__)  # Initialise the Sum array

        for a in neigh:  # For each adjacent
            roll = self.__lattice__.copy()

            for j in dim:  # For each dimension

                roll = np.roll(roll, adj[a, j], axis=j)

            Sum += J[a] * roll

        return Sum

    def randomize(self, ratio=0.5):
        """
        Randomize the lattice state.

        Parameters:
            ratio: float
                The ratio between the up state and the size of the array
        """
        size = self.__lattice__.size
        _lattice = self.__lattice__
        shape = self.__shape__

        _lattice[...] = (__randm__(*shape) <= ratio) * 2 - 1

        closest_ratio = int(size * ratio)

        val = closest_ratio - (self == 1).sum()

        if val != 0:
            flips = abs(val)
            sign = val / flips
            mask = self == -sign
            n = mask.sum()
            choice = np.random.permutation(n)[:flips]

            mask = np.where(mask)
            indices = tuple()
            for d in range(self.dim):
                indices += tuple([mask[d][choice]])

            _lattice[indices] = sign

    def all(self, state):
        """
        Set all the lattice to the same state.

        Parameters:
            state: -1 or 1
                value of the spin site
        """

        self.__lattice__[...] = state

    def mag(self):
        """
        Compute the magnetization of the lattice
        """
        return self.__lattice__.mean()

    def hamiltonian(self):
        """
        Compute the Halmitonian of each spin
        """
        return -self.__lattice__ * (self.__sum_adj__() + self.B)

    def H(self):
        """
        Compute the Hamiltonian of the lattice
        """
        return self.hamiltonian().sum()

    def mH(self):
        """
        Compute the mean value of the Hamiltonian
        """
        return self.hamiltonian().mean()

    def get_state(self):
        """
        Traditionnal method to get the state of the lattice
        """
        return self.__lattice__.copy()

    def set_state(self, state):
        """
        Traditionnal method to set the state of the lattice
        """
        self.__lattice__ = state.copy()
