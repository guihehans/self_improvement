#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: kth_smallest_number.py
@time: 2021/1/7 9:53
@function:

"""

from heapq import *


def find_Kth_smallest_number(nums, k):
    max_heap = []
    for i in range(len(nums)):
        if i < k:
            heappush(max_heap, -nums[i])
        else:
            if nums[i] < -max_heap[0]:
                heappushpop(max_heap, -nums[i])
            else:
                continue

    return -max_heap[0]


def test():
    nums = [1, 5, 12, 2, 11, 5]
    k = 3
    result = 5
    assert find_Kth_smallest_number(nums, k) == result


def test_1():
    nums = [1, 5, 12, 2, 11, 5]
    k = 4
    result = 5
    assert find_Kth_smallest_number(nums, k) == result


def test_2():
    nums = [5, 12, 11, -1, 12]
    k = 3
    result = 11
    assert find_Kth_smallest_number(nums, k) == result


if __name__ == '__main__':
    test()
