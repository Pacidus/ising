#!/usr/bin/env python3
# coding:utf-8

"""
@author: Pacidus

A module for the Ising model
"""

__version__ = "0.1.0"

import numpy as np

# Alias for np.random.rand
__rand__ = np.random.rand
# Alias for np.random.randint
__randint__ = np.random.randint


class lattice:
    """
    Lattice: the main place of the Ising model.
       
    Parameters:
        shape: tuple
            The shape of the lattice
    """

    def __init__(self, shape, *args, **kwargs):
        self.__shape__ = shape
        self.__lattice__ = np.empty(shape)

        self.shape = self.__shape__
        self.size = 1
        self.dim = len(shape)

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
                    vec = [0]*self.dim
                    vec[j] = i*2 -1
                    adj.append(vec)
                    
            self.adj = np.array(adj)

        self.J = np.ones(self.adj.shape[0])
        
        if "J" in kwargs:
            self.J *= kwargs["J"]

    def __sum__(self):
        """
        Sum the adjacents
        """

        J = self.J  # The interaction
        adj = self.adjacent  # The vector of the adjacent

        n, d = adj.shape  # n: number of adjacent, d: the dimension

        dim = range(d)
        neigh = range(n)

        Sum = np.zeros(*self.__shape__)  # Initialise the Sum array

        for a in adj:  # For each adjacent
            roll = self.__lattice__

            for j in run:  # For each dimension

                roll = np.roll(roll, adj[a, j], axis=j)

            Sum += J[a] * roll

        return Sum

    def __eq__(self, value):
        return self.__lattice__ == value

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

        _lattice[...] = (__rand__(*shape) <= ratio) * 2 - 1

        closest_ratio = int(size * ratio)

        val = closest_ratio - (self == 1).sum()

        if val != 0:
            flips = abs(val)
            sign = val / flips
            mask = self == -sign
            n = mask.sum()
            choice = np.random.permutation(n)[:flips]
            mask1, mask2 = np.where(mask)
            _lattice[mask1[choice], mask2[choice]] = sign

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
        Compute the magnetization of the lattice
        """

    def energy(self):
        return self.__lattice__.mean()
