# coding:utf-8

"""
@author: Pacidus

A module for the metropolis algorithm
"""

from ising import lattice
import numpy as np


class algorithm(lattice):
    """
    Implementation of the metropolis algorithm

    for the arguments look the lattice class 
    """

    def __init__(self, shape, *args, **kwargs):
        super().__init__(shape, *args, **kwargs)

        self.M = []

    def __n__(self, v=0.001):
        a = v / self.adj.shape[0]
        b = self.size - 1
        n = int((a * b + 1) / (a + 1))
        if n <= 0:
            n = 1

        self.__On__ = n

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
