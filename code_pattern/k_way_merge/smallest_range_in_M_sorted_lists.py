#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: smallest_range_in_M_sorted_lists.py
@time: 2021/1/22 14:18
@function:

"""
import collections
import math
from heapq import *


def find_smallest_range_my(lists):
    min_heap = []
    range_start, range_end = 0, math.inf
    cur_max = -math.inf
    for arr in lists:
        heappush(min_heap, (arr[0], 0, arr))
        cur_max = max(cur_max, arr[0])

    while len(min_heap) == len(lists):
        value, i, arr = heappop(min_heap)
        if cur_max - value < range_end - range_start:  # when cur range less, update range.
            range_start = value
            range_end = cur_max

        if (i + 1) < len(arr):  # popped list has next num to push,heappush.
            heappush(min_heap, (arr[i + 1], i + 1, arr))
            cur_max = max(cur_max, arr[i + 1])

    return [range_start, range_end]


def find_smallest_range(nums):
    n = len(nums)
    cur_min, cur_max = math.inf, -math.inf

    indices = collections.defaultdict(list)

    for i, arr in enumerate(nums):
        for x in arr:
            indices[x].append(i)
            cur_max = max(cur_max, *arr)
            cur_min = min(cur_min, *arr)

    freq = [0] * n
    left, right = cur_min, cur_min - 1
    best_left, best_right = cur_min, cur_max
    inside = 0

    while right < cur_max:
        right += 1
        if right in indices:
            for x in indices[right]:
                freq[x] += 1
                if freq[x] == 1:
                    inside += 1
        while inside == n:
            if right - left < best_right - best_left:
                best_left, best_right = left, right
            if left in indices:
                for x in indices[left]:
                    freq[x] -= 1
                    if freq[x] == 0:
                        inside -= 1
            left += 1

    return [best_left, best_right]


def test():
    lists = [[1, 5, 8], [4, 12], [7, 8, 10]]
    expected = [4, 7]
    assert find_smallest_range(lists) == expected


def test_1():
    lists = [[1], [2], [3], [4], [5], [6], [7]]
    expected = [1, 7]
    assert find_smallest_range(lists) == expected


def test_2():
    lists = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    expected = [1, 1]
    assert find_smallest_range(lists) == expected


def test_3():
    lists = [[-1, 2, 3], [1], [1, 2], [1, 1, 3]]
    expected = [1, 2]
    assert find_smallest_range(lists) == expected


if __name__ == '__main__':
    test()
