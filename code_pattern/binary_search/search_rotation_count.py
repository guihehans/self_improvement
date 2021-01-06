#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: search_rotation_count.py
@time: 2021/1/6 15:32
@function:

"""


def count_rotations(arr):
    n = len(arr)
    start, end = 0, n - 1
    if arr[start] < arr[end]:
        return 0

    while start < end and end - start != 1:
        mid = start + ((end - start) >> 1)
        if arr[start] <= arr[mid]:  # [start,mid] ordered.
            start = mid
        elif arr[mid] <= arr[end]:
            end = mid

    peak_index = start

    return peak_index + 1


def test():
    assert (count_rotations([10, 15, 1, 3, 8])) == 2


def test_1():
    assert (count_rotations([4, 5, 7, 9, 10, -1, 2])) == 5


def test_2():
    assert (count_rotations([1, 3, 8, 10])) == 0


if __name__ == '__main__':
    test()
