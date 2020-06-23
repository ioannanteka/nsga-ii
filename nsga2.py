#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:14:48 2020

@author: Ioanna Nteka
"""

class NSGA2:
    ''' NSGA-2 for multiobjective optimization. Used to obtain the Pareto front
    of a collection of points in a multidimensional space.

    Parameters
    ----------
    objective : a function
        The function to minimize typically from R^n to R^m with m >= 1
    in_dim : integer
        The dimension of the input
    out_dim : integer
        The dimension of the output

    Notes
    -----
    The algorithm implemented is described in Pratap, Agarwal and Meyarivan
    2002.
    '''

    def __init__(self, objective, in_dim, out_dim):
        self.objective = objective
        self.in_dim = in_dim
        self.out_dim = out_dim
    