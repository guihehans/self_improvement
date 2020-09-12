#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: brutal_force.py
@time: 2020/9/9 10:42
@function:
the Brutal-Force method to find  the first occurrence of a pattern string in a
    text string.
Time complexity is proportionally O(n*m) where n is length of text string and m is length of pattern string

"""


class BrutalForce:
    def __init__(self):
        pass

    @staticmethod
    def search(text: str, pattern: str):
        n = len(text)
        m = len(pattern)
        for i in range(n - m):
            if text[i:i + m] == pattern:
                return i
        return -1


if __name__ == '__main__':
    test_string = "abcdggn"
    pattern = 'cdg'
    index = BrutalForce.search(test_string, pattern)
    print(index)
