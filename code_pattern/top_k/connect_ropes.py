#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: connect_ropes.py
@time: 2021/1/7 14:55
@function:

"""

from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    min_heap = []
    result = 0

    # build min heap
    for i in range(len(ropeLengths)):
        heappush(min_heap, ropeLengths[i])

    while len(min_heap) > 1:
        rope_1 = heappop(min_heap)
        rope_2 = heappop(min_heap)
        new_rope = rope_1 + rope_2
        heappush(min_heap, new_rope)
        result += new_rope

    return result


def test():
    arr = [1, 3, 11, 5]
    expected = 33
    assert minimum_cost_to_connect_ropes(arr) == expected


def test_2():
    arr = [3, 4, 5, 6]
    expected = 36
    assert minimum_cost_to_connect_ropes(arr) == expected


def test_3():
    arr = [1, 3, 11, 5, 2]
    expected = 42
    assert minimum_cost_to_connect_ropes(arr) == expected


if __name__ == '__main__':
    test()
