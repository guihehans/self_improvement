#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: search_rotated_array.py
@time: 2021/1/4 17:49
@function:

"""


def search_rotated_array(arr, key):
    n = len(arr)
    start, end = 0, n - 1

    while start < end:
        mid = start + ((end - start) >> 1)
        if mid + 1 < n:
            if arr[mid] > arr[mid -1]:
                end = mid
            else:
                start = mid + 1
    return -1


def test():
    assert search_rotated_array([10, 15, 1, 3, 8], 15) == 1


def test_1():
    assert search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10) == 4


def test_2():
    assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_null():
    assert search_rotated_array([0], 1) == -1


if __name__ == '__main__':
    test()
