#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: kth_largest_in_stream.py
@time: 2021/1/7 16:48
@function:

"""

from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.min_heap = []
        for i in range(len(nums)):
            if i < k:
                heappush(self.min_heap, nums[i])
            else:
                if nums[i] > self.min_heap[0]:
                    heappushpop(self.min_heap, nums[i])
        self.k = k

    def add(self, num):
        heappush(self.min_heap, num)
        if len(self.min_heap > self.k):
            heappop(self.min_heap)
        return self.min_heap[0]


def test():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    assert kthLargestNumber.add(6) == 5
    assert kthLargestNumber.add(13) == 6
    assert kthLargestNumber.add(4) == 6


def test_1():
    kthLargestNumber = KthLargestNumberInStream([0], 2)
    assert kthLargestNumber.add(-1) == -1
    assert kthLargestNumber.add(1) == 0
    assert kthLargestNumber.add(-2) == 0
    assert kthLargestNumber.add(-4) == 0
    assert kthLargestNumber.add(3) == 1


def test_null():
    kthLargestNumber = KthLargestNumberInStream([], 1)
    assert kthLargestNumber.add(-3) == -3
    assert kthLargestNumber.add(-2) == -2
    assert kthLargestNumber.add(-4) == -2
    assert kthLargestNumber.add(0) == 0
    assert kthLargestNumber.add(4) == 4


if __name__ == '__main__':
    test()
