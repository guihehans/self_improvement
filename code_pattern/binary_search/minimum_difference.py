#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: minimum_difference.py
@time: 2020/12/31 15:53
@function:

"""


def search_min_diff_element(arr, key):
    n = len(arr)
    start, end = 0, n - 1
    if key <= arr[0]:
        return arr[0]
    if key >= arr[end]:
        return arr[end]

    while start <= end:
        mid = start + ((end - start) >> 1)
        mid_value = arr[mid]
        if key == mid_value:
            return mid_value
        elif key < mid_value:
            end = mid - 1
        else:
            start = mid + 1
    # when loop end, start is larger one, end is smaller one.
    if arr[start] - key <= key - arr[end]:
        return arr[start]
    else:
        return arr[end]


def test():
    assert (search_min_diff_element([4, 6, 10], 17)) == 10


def test_1():
    assert (search_min_diff_element([4, 6, 10], 7)) == 6


def test_2():
    assert (search_min_diff_element([4, 6, 10], 4)) == 4


def test_3():
    assert (search_min_diff_element([1, 3, 8, 10, 15], 12)) == 10


if __name__ == '__main__':
    test()
