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

    while start <= end:
        mid = start + ((end - start) >> 1)
        if key == arr[mid]:
            return mid
        if arr[start] <= arr[mid]:  # 前半段有序
            if arr[start] <= key < arr[mid]:  # key 在有序前半段中
                end = mid - 1
            else:  # key 在后半段中
                start = mid + 1
        else:  # 后半段有序
            if arr[mid] < key <= arr[end]:  # key 在有序后半段中
                start = mid + 1
            else:  # key 在前半段
                end = mid - 1

    return -1


def test():
    assert search_rotated_array([10, 15, 1, 3, 8], 15) == 1


def test_1():
    assert search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10) == 4


def test_2():
    assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_null():
    assert search_rotated_array([0], 1) == -1


def test_asc():
    assert search_rotated_array([0, 3, 5], 5) == 2


if __name__ == '__main__':
    test()
