#!/usr/bin/env python3
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
    """

    def __init__(cls, shape):
        super().__init__(shape)
