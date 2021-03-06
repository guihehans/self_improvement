#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: ceiling_of_number.py
@time: 2020/12/30 13:47
@function:

"""


def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    start, end = 0, n - 1
    if key > arr[end]:
        return -1

    while start <= end:
        mid = start + ((end - start) >> 1)
        mid_val = arr[mid]
        if key == mid_val:
            return mid
        elif key < mid_val:
            end = mid - 1
        else:
            start = mid + 1
    return start


def test():
    assert (search_ceiling_of_a_number([4, 6, 10], 6)) == 1
    assert (search_ceiling_of_a_number([1, 3, 8, 10, 15], 7)) == 2
    assert (search_ceiling_of_a_number([1, 3, 8, 10, 15], 12)) == 4
    assert (search_ceiling_of_a_number([4, 6, 10], 17)) == -1
    assert (search_ceiling_of_a_number([4, 6, 10], -1)) == 0


if __name__ == '__main__':
    test()
