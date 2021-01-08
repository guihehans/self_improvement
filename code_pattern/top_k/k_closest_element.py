#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: k_closest_element.py
@time: 2021/1/8 9:26
@function:

"""

from heapq import *
from collections import deque


def find_closest_elements(arr, K, X):
    n = len(arr)

    idx = binary_search(arr, X)
    start, end = idx - K, idx + K
    start = max(start, 0)
    end = min(end, n - 1)

    min_heap = []
    for i in range(start, end + 1):
        heappush(min_heap, (get_dist(X, arr[i]), arr[i]))

    result = [0] * K
    for i in range(K):
        result[i] = heappop(min_heap)[1]
    return sorted(result)


def binary_search(arr, key):
    n = len(arr)
    start, end = 0, n - 1
    while start < end:
        mid = start + ((end - start) >> 1)
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    # normally start-1 is the element index<key.
    # if the index is zero, return start.
    if start > 0:
        return start - 1
    return start


def get_dist(X, Y):
    return abs(Y - X)


def test():
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    expected = [1, 2, 3, 4]
    assert set(find_closest_elements(arr, k, x)) == set(expected)


def test_1():
    arr = [2, 4, 5, 6, 9]
    k = 3
    x = 6
    expected = [4, 5, 6]
    assert set(find_closest_elements(arr, k, x)) == set(expected)


def test_2():
    arr = [2, 4, 5, 6, 9]
    k = 3
    x = 10
    expected = [5, 6, 9]
    assert set(find_closest_elements(arr, k, x)) == set(expected)


def test_3():
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    expected = [1, 2, 3, 4]
    assert set(find_closest_elements(arr, k, x)) == set(expected)


if __name__ == '__main__':
    test()
