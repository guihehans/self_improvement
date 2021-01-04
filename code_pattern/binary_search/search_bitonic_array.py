#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: search_bitonic_array.py
@time: 2021/1/4 15:43
@function:

"""


def search_bitonic_array(arr, key):
    n = len(arr)
    start, end = 0, n - 1

    while start < end:
        mid = start + ((end - start) >> 1)
        if mid + 1 < n:
            if arr[mid] > arr[mid + 1]:
                end = mid
            else:
                start = mid + 1

    max_index = start
    idx_1 = binary_search(arr, 0, max_index, key)
    if idx_1 == -1:
        idx_2 = binary_search(arr, max_index, n - 1, key)
        return idx_2
    else:
        return idx_1


# order-agnostic binary search
def binary_search(arr, start, end, key):
    while start <= end:
        mid = start + ((end - start) >> 1)
        if key == arr[mid]:
            return mid
        # ascending order
        if arr[start] < arr[end]:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:  # descending order
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8, 3, 4, 7], 10))


main()
