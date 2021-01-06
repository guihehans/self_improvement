#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_k_largest.py
@time: 2021/1/6 17:40
@function:

"""

from heapq import *


def find_k_largest_numbers(nums, k):
    min_heap = []
    for i in range(len(nums)):
        if i < k:
            heappush(min_heap, nums[i])
        else:
            if nums[i] <= min_heap[0]:
                continue
            else:
                heappushpop(min_heap, nums[i])
    return list(min_heap)


def test():
    arr = [3, 1, 5, 12, 2, 11]
    k = 3
    result = (find_k_largest_numbers(arr, k))
    ans = [12, 11, 5]
    assert set(ans) == set(result)


def test_1():
    arr = [5, 12, 11, -1, 12]
    k = 3
    result = (find_k_largest_numbers(arr, k))
    ans = [12, 11, 12]
    assert set(ans) == set(result)


if __name__ == '__main__':
    test()
