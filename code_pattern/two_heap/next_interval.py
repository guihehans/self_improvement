#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: next_interval.py
@time: 2020/12/21 17:52
@function:

"""

from typing import *
from heapq import *


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1 for _ in range(n)]
        if n < 2:
            return result

        entry = list(zip(intervals, range(n)))  # get a list like: [(interval_list,index)]
        # sort the entry by interval_list[0], which is the interval start
        sorted_intervals = sorted(entry, key=lambda x: x[0][0])

        for i in range(n):
            interval = intervals[i]
            end = interval[1]
            # if current interval end > largest interval's start, no interval found, return -1
            if end > sorted_intervals[-1][0][1]:
                result[i] = -1
            # else binary search the index in sorted entry
            else:
                index = binary_search(sorted_intervals, end)
                result[i] = index

        return result


def binary_search(arr, value):
    start = 0
    end = len(arr) - 1

    while start <= end:
        # to avoid start+end overflow and bit operate is faster, use current start+((end-start)>>1)
        # which is start+(end-start)/2
        mid = start + ((end - start) >> 1)
        mid_value = arr[mid][0][0]

        if mid_value >= value:
            if mid == 0 or (arr[mid - 1][0][0] < value):
                return arr[mid][1]
            else:
                end = mid - 1
        elif mid_value < value:
            start = mid + 1
    return -1


def find_next_interval(intervals):
    n = len(intervals)

    # heaps for finding the maximum start and end
    maxStartHeap, maxEndHeap = [], []

    result = [0 for x in range(n)]
    for endIndex in range(n):
        heappush(maxStartHeap, (-intervals[endIndex][0], endIndex))
        heappush(maxEndHeap, (-intervals[endIndex][1], endIndex))

    # go through all the intervals to find each interval's next interval
    for _ in range(n):
        # let's find the next interval of the interval which has the highest 'end'
        topEnd, endIndex = heappop(maxEndHeap)
        result[endIndex] = -1  # defaults to - 1
        if -maxStartHeap[0][0] >= -topEnd:
            topStart, startIndex = heappop(maxStartHeap)
            # find the the interval that has the closest 'start'
            while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            result[endIndex] = startIndex
            # put the interval back as it could be the next interval of other intervals
            heappush(maxStartHeap, (topStart, startIndex))

    return result


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


def test_null():
    s = Solution()
    arr = []
    assert s.findRightInterval(arr) == []


def test_one_element():
    s = Solution()
    arr = [[1, 2]]
    assert s.findRightInterval(arr) == [-1]


def test_l():
    s = Solution()
    arr = [[3, 4], [1, 2], [2, 3], [1, 5], [5, 9], [9, 10]]
    assert s.findRightInterval(arr) == [4, 2, 0, 4, 5, -1]
    assert find_next_interval(arr) == [4, 2, 0, 4, 5, -1]


if __name__ == '__main__':
    test()
    test_1()
    test_2()
