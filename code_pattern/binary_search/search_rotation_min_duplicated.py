#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: search_rotation_min_duplicated.py
@time: 2021/1/6 16:12
@function:

"""


def find_rotation_count_duplicated(arr):
    n = len(arr)
    start, end = 0, n - 1

    while start < end:
        mid = start + ((end - start) >> 1)
        if mid < end and arr[mid] > arr[mid + 1]:  # found pivot point mid+1
            return mid + 1
        if start < mid and arr[mid - 1] > arr[mid]:  # found pivot mid
            return mid

        # if start==mid==end, check if start or end is min before update them.
        if arr[start] == arr[mid] == arr[end]:
            if arr[start] > arr[start + 1]:
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:
                return end
            end -= 1

        elif arr[start] <= arr[mid]:  # [start,mid] ordered.
            start = mid + 1
        elif arr[mid] <= arr[end]:
            end = mid - 1
    return 0


def test():
    assert (find_rotation_count_duplicated([10, 15, 1, 3, 3, 3, 8])) == 2


def test_1():
    assert (find_rotation_count_duplicated([4, 5, 7, 9, 10, -1, -1, -1, 2])) == 5


def test_2():
    assert (find_rotation_count_duplicated([10, 1, 10, 10, 10])) == 1


def test_3():
    assert (find_rotation_count_duplicated([2, 2, 2, 0, 1])) == 3


def test_4():
    assert (find_rotation_count_duplicated([3, 1, 3])) == 1


def test_5():
    assert (find_rotation_count_duplicated([10, 10, 10, 1, 10])) == 3


def test_6():
    assert (find_rotation_count_duplicated([10, 10, 10, 1,1, 1,1, 1, 1])) == 3


def test_7():
    assert (find_rotation_count_duplicated([3, 3, 1, 2, 3, 3, 3, 3])) == 2


def test_8():
    assert (find_rotation_count_duplicated([1, 1, 1, 3, 1])) == 4


def test_single():
    assert (find_rotation_count_duplicated([1])) == 0


def test_double():
    assert (find_rotation_count_duplicated([1, 1])) == 0


if __name__ == '__main__':
    test()
