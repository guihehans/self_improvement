#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: kmp.py
@time: 2020/9/18 9:51
@function:

THe KMP algorithm, compare from left to right.
Time : O(N+M)
space: O(M)
"""
from typing import List


class KMP:

    def __init__(self, pattern):
        self.pattern = pattern
        self.M = len(pattern)
        self.next = self.generate_next(pattern, self.M)

    def generate_next(self, pattern, M) -> List[int]:
        """
        the next array(also called failure function),store the prefix's longest match sub prefix info.

        the index is the prefix's ending char index,range from [0,M-1],

        the value is the longest suffix match sub prefix's ending char index.-1 if not exist.

        :param pattern: the pattern string
        :param M: length of pattern
        :return:next_arr
        """
        next_arr = []
        return next_arr

    def search(self, txt):
        N = len(txt)
        M = self.M
        pattern = self.pattern
        next = self.next
        j = 0
        for i in range(N):
            while j > 0 and txt[i] != pattern[j]:
                j = next[j - 1] + 1
            if txt[i] == pattern[j]:
                j += 1
            if j == M:
                return i - M + 1

        return N
