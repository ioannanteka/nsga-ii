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
    data : (N, K) array-like
        The candidate data points for the Pareto front.

    Notes
    -----
    The algorithm implemented is described in Pratap, Agarwal and Meyarivan
    2002.
    '''

    def __init__(self, data):
        self.data = data
        self.dim = data.shape[1]
    