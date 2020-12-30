#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: order_agnostic_binary_search.py
@time: 2020/12/29 17:58
@function:

"""


def binary_search(arr, key):
    start, end = 0, len(arr) - 1

    direction = True if arr[start] < arr[end] else False

    while start <= end:
        # the parenthesis is important!
        mid = start + ((end - start) >> 1)
        if key == arr[mid]:
            return mid
        else:
            if (direction and key > arr[mid]) or (not direction and key < arr[mid]):
                start = mid + 1
            else:
                end = mid - 1

    return -1


def test():
    assert (binary_search([4, 6, 10], 10)) == 2
    assert (binary_search([1, 2, 3, 4, 5, 6, 7], 5)) == 4
    assert (binary_search([10, 6, 4], 10)) == 0
    assert (binary_search([10, 6, 4], 4)) == 2
    assert (binary_search([10, 6, 4], 7)) == -1


if __name__ == '__main__':
    test()
