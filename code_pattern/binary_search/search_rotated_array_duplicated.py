#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: search_rotated_array_duplicated.py
@time: 2021/1/6 14:25
@function:

"""


def search_rotated_array_duplicated(arr, key):
    n = len(arr)
    start, end = 0, n - 1

    while start <= end:
        mid = start + ((end - start) >> 1)
        if key == arr[mid]:
            return True
        if arr[mid] == arr[start] == arr[end]:
            start = start + 1
            end = end - 1
        elif arr[start] <= arr[mid]:
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return False


def test():
    assert search_rotated_array_duplicated([10, 15, 1, 1, 3, 3, 3, 8], 15) is True


def test_1():
    assert search_rotated_array_duplicated([4, 5, 7, 7, 9, 9, 9, 10, -1, 2], 10) is True


def test_2():
    assert search_rotated_array_duplicated([2, 5, 6, 0, 0, 1, 2], 0) is True


def test_null():
    assert search_rotated_array_duplicated([0, 0], 1) is False


def test_asc():
    assert search_rotated_array_duplicated([0, 3, 3, 3, 5], 5) is True


if __name__ == '__main__':
    test()
