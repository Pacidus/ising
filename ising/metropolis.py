# coding:utf-8

"""
@author: Pacidus

A module for the metropolis algorithm
"""

from ising import lattice
import numpy as np

# Alias for np.random.rand
__randm__ = np.random.rand


class algorithm(lattice):
    """
    Implementation of the metropolis algorithm

    for the arguments look the lattice class 
    """

    def __init__(self, shape, *args, **kwargs):
        super().__init__(shape, *args, **kwargs)

        if "v" in kwargs:
            self.__n__(kwargs["v"])
        else:
            self.__n__()

    def __n__(self, v=0.001):
        """
        Compute the value of n given a probability v
        """
        a = v / self.adj.shape[0]
        b = self.size - 1
        n = int((a * b + 1) / (a + 1))
        if n <= 0:
            n = 1

        self.__On__ = n

    def __sac__(self, choice):
        """
        Sum Adjacents Choice contribution of the hamiltionian
        """

        J = self.J  # The interaction
        adj = self.adj  # The vector of the adjacent

        a, d = adj.shape  # a: number of adjacent, d: the dimension
        n = self.__choice__[0].size  # n: choice size

        Sum = np.zeros(n)

        dim = range(d)
        nei = range(a)

        for j in nei:
            roll = choice[:]
            roll = tuple([(roll[k] + adj[j, k]) % self.__shape__[k] for k in dim])
            Sum += self.J[j] * self.get_state()[roll]

        return Sum

    def __DH__(self, choice):
        """
        Compute the delta in energy for a set of spin flip 
        """
        return 2 * self.__lattice__[choice] * (self.__sac__(choice) + self.B[choice])

    def __Ptrans__(self, choice):
        """
        Return the proba of transition
        """
        return np.exp(-self.beta * self.__DH__(choice))

    def step(self, n=0):
        """
        step apply the metropolis algorithm n times once

        Parameters:
        
            optionnal:

            n: **int** > 0

            n is the number of flip in one step
        """

        if n <= 0:
            n = self.__On__

        self.__choice__ = tuple()
        for i in self.__shape__:
            self.__choice__ += (np.random.permutation(i)[:n],)

        self.__lattice__[self.__choice__] *= 1 - 2 * (
            __randm__(n) <= self.__Ptrans__(self.__choice__)
        )
