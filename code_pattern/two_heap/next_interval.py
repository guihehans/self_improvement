#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: next_interval.py
@time: 2020/12/21 17:52
@function:

"""

from typing import *


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        max_heap = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] > sorted_intervals[-1][1]:
                result.append(-1)
            else:
                index = binary_search(sorted_intervals, interval[1])
                result.append(index)

        return result


def binary_search(arr, value):
    start = 0
    end = len(arr) - 1

    while start <= end:
        # to avoid start+end overflow and bit operate is faster, use current start+((end-start)>>1)
        # which is start+(end-start)/2
        mid = start + ((end - start) >> 1)
        mid_value = arr[mid][0]

        if mid_value >= value:
            if mid == 0 or (arr[mid - 1][0] < value):
                return mid
            else:
                end = mid - 1
        elif mid_value < value:
            start = mid + 1
    return -1


def test():
    s = Solution()
    arr = [[2, 3], [3, 4], [5, 6]]
    result = s.findRightInterval(arr)
    assert result == [1, 2, -1]


def test_1():
    s = Solution()
    arr = [[3, 4], [1, 5], [4, 6]]
    result = s.findRightInterval(arr)
    assert result == [2, -1, -1]


def test_2():
    s = Solution()
    arr = [[3, 4], [2, 3], [1, 2]]
    result = s.findRightInterval(arr)
    assert result == [-1, 0, 1]


if __name__ == '__main__':
    test()
    test_1()
    test_2()
