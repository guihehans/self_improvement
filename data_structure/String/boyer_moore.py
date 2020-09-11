#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: boyer_moore.py
@time: 2020/9/11 16:54
@function:

"""


class BoyerMoore:
    def __init__(self, pattern):
        self.pat = pattern
        self.M = len(pattern)
        # ascii size
        self.R = 256
        # a hashtable with R size, called bad characters bc
        self.bc = [-1 for i in range(0, self.R)]
        # store the latest index for characters in pattern, in corresponding index of ascii value in bc
        for j in range(self.M):
            self.bc[ord(pattern[j])] = j

    def search(self, txt):
        pass
