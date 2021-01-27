#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: k_pairs_with_largest_sum.py
@time: 2021/1/26 17:10
@function:

"""

from __future__ import print_function
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
    min_heap = []
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heappushpop(min_heap, (nums1[i] + nums2[j], i, j))

    result = []
    for sum_val, i, j in min_heap:
        result.append([nums1[i], nums2[j]])

    return result


def test():
    nums_1 = [9, 8, 2]
    nums_2 = [6, 3, 1]
    k = 3
    expected = [[9, 3], [9, 6], [8, 6]]
    result = find_k_largest_pairs(nums_1, nums_2, k)
    assert len(expected) == len(result)
    for item in expected:
        assert item in result


def test_1():
    nums_1 = [5, 2, 1]
    nums_2 = [2, -1]
    k = 3
    expected = [[5, 2], [5, -1], [2, 2]]
    result = find_k_largest_pairs(nums_1, nums_2, k)
    assert len(expected) == len(result)
    for item in expected:
        assert item in result


if __name__ == '__main__':
    test()
