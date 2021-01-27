#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: k_pairs_with_smallest_sum.py
@time: 2021/1/27 11:28
@function:

"""
from typing import List
from heapq import *


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(max_heap) < k:
                    heappush(max_heap, (-(nums1[i] + nums2[j]), i, j))
                else:
                    cur_sum = -(nums1[i] + nums2[j])
                    if cur_sum < max_heap[0][0]:
                        break
                    else:
                        heappushpop(max_heap, (-(nums1[i] + nums2[j]), i, j))
        result = []
        for sum_value, i, j in max_heap:
            result.append([nums1[i], nums2[j]])
        return result


def test():
    nums_1 = [1, 7, 11]
    nums_2 = [2, 4, 6]
    k = 3
    expected = [[1, 2], [1, 4], [1, 6]]
    s = Solution()
    result = s.kSmallestPairs(nums_1, nums_2, k)
    assert len(expected) == len(result)
    for item in expected:
        assert item in result


def test_1():
    nums_1 = [1, 1, 2]
    nums_2 = [1, 2, 3]
    k = 2
    expected = [[1, 1], [1, 1]]
    s = Solution()
    result = s.kSmallestPairs(nums_1, nums_2, k)
    assert len(expected) == len(result)
    for item in expected:
        assert item in result


if __name__ == '__main__':
    test()
