#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_unique_trees_to_store_n.py
@time: 2020/12/28 16:18
@function:

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def find_unique_trees(self, n):
        return G(n)


def G(N):
    G = [0] * (N + 1)
    G[0], G[1] = 1, 1
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            G[i] += G[j - 1] * G[i - j]

    return G[N]


def test():
    N = 2
    result = 2
    s = Solution()
    assert s.find_unique_trees(N) == result


def test_1():
    N = 3
    result = 5
    s = Solution()
    assert s.find_unique_trees(N) == result


def test_3():
    N = 4
    result = 14
    s = Solution()
    assert s.find_unique_trees(N) == result


def test_4():
    N = 5
    result = 42
    s = Solution()
    assert s.find_unique_trees(N) == result


if __name__ == '__main__':
    print(G(5))
