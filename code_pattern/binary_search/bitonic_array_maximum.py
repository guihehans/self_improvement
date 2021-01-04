#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: bitonic_array_maximum.py
@time: 2021/1/4 11:00
@function:

"""


def find_max_in_bitonic_array(arr):
    n = len(arr)
    start, end = 0, n - 1
    while start < end:
        mid = start + ((end - start) >> 1)
        if mid + 1 < n:
            if arr[mid] > arr[mid + 1]:
                end = mid
            else:
                start = mid + 1

    return arr[start]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
