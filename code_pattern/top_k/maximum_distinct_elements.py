#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: maximum_distinct_elements.py
@time: 2021/1/8 14:48
@function:

"""

from heapq import *


def find_maximum_distinct_elements(nums, k):
    freq_map = {}
    unique_count = 0
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    min_heap = []
    for key, freq in freq_map.items():
        if freq > 1:
            heappush(min_heap, (freq, key))
        else:
            unique_count += 1

    i = 0
    while i < k and min_heap:
        freq, num = min_heap[0]
        freq_map[num] -= 1
        if freq_map[num] == 1:
            heappop(min_heap)
            unique_count += 1
        i += 1

    while i < k:
        unique_count -= 1
        i += 1

    distinct_size = unique_count
    return distinct_size


def test():
    arr = [7, 3, 5, 8, 5, 3, 3]
    k = 2
    expected = 3
    assert find_maximum_distinct_elements(arr, k) == expected


def test_1():
    arr = [3, 5, 12, 11, 12]
    k = 3
    expected = 2
    assert find_maximum_distinct_elements(arr, k) == expected


def test_2():
    arr = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
    k = 2
    expected = 3
    assert find_maximum_distinct_elements(arr, k) == expected


if __name__ == '__main__':
    test()
