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


def find_closest_elements_heap(arr, K, X):
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
    while start <= end:
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


def find_closest_elements(arr, K, X):
    n = len(arr)

    idx = binary_search(arr, X)
    start, end = idx, idx + 1

    result = deque()
    for i in range(K):
        if start >= 0 and end <= n - 1:
            if X - arr[start] <= arr[end] - arr[idx]:
                result.appendleft(arr[start])
                start -= 1
            else:
                result.append(arr[end])
                end += 1
        elif start >= 0:  # end reach n-1
            result.appendleft(arr[start])
            start -= 1
        elif end <= n - 1:  # start reach 0
            result.append(arr[end])
            end += 1
    return list(result)


def find_closest_elements_x(arr, K, X):
    result = deque()
    index = binary_search(arr, X)
    leftPointer, rightPointer = index, index + 1
    n = len(arr)
    for i in range(K):
        if leftPointer >= 0 and rightPointer < n:
            diff1 = abs(X - arr[leftPointer])
            diff2 = abs(X - arr[rightPointer])
            if diff1 <= diff2:
                result.appendleft(arr[leftPointer])
                leftPointer -= 1
            else:
                result.append(arr[rightPointer])
                rightPointer += 1
        elif leftPointer >= 0:
            result.appendleft(arr[leftPointer])
            leftPointer -= 1
        elif rightPointer < n:
            result.append(arr[rightPointer])
            rightPointer += 1

    return result


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


def test_4():
    arr = [1, 1, 1, 10, 10, 10]
    k = 1
    x = 9
    expected = [10]
    assert set(find_closest_elements(arr, k, x)) == set(expected)


def test_5():
    arr = [0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 7, 9, 9, 10, 10, 11, 11, 12, 13, 14, 14, 15, 17, 19, 19, 22, 24, 24, 25, 25,
           27, 27, 29, 30, 32, 32, 33, 33, 35, 36, 38, 39, 41, 42, 43, 44, 44, 46, 47, 48, 49, 52, 53, 53, 54, 54, 57,
           57, 58, 59, 59, 59, 60, 60, 60, 61, 61, 62, 64, 66, 68, 68, 70, 72, 72, 74, 74, 74, 75, 76, 76, 77, 77, 80,
           80, 82, 83, 85, 86, 87, 87, 92, 93, 94, 96, 96, 97, 98, 99]
    k = 25
    x = 90
    expected = [72, 74, 74, 74, 75, 76, 76, 77, 77, 80, 80, 82, 83, 85, 86, 87, 87, 92, 93, 94, 96, 96, 97, 98, 99]
    assert (find_closest_elements(arr, k, x)) == (expected)


if __name__ == '__main__':
    test()
