#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: rabin_karp.py
@time: 2020/9/9 15:34
@function:

This is a Rabin-Karp(RK) algorithm implementation

"""


class RabinKarp:
    def __init__(self, pattern: str):
        """
        init function

        :param pattern: the pattern string to search
        :param R: the alphabet size or radix
        """
        self.pat = pattern
        # ascii set size
        self.R = 256
        self.m = len(pattern)
