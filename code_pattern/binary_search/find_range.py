#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_range.py
@time: 2020/12/31 11:04
@function:

"""


def find_range(arr, key):
    result = [- 1, -1]
    result[0] = binary_search_max(arr, key, find_first=True)
    if result[0] != -1:
        result[1] = binary_search_max(arr, key, find_first=False)
    return result


def binary_search_max(arr, key, find_first):
    """
    a util function to search first index of key OR last index.
    :param arr:
    :param key:
    :param find_first: True, return first index. otherwise return last
    :return:
    """
    n = len(arr)
    start, end = 0, n - 1
    key_index = -1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # key==arr[mid]
            key_index = mid
            if find_first:  # move towards first index
                end = mid - 1
            else:  # move towards last index
                start = mid + 1

    return key_index


def test():
    assert (find_range([4, 6, 6, 6, 9], 6)) == [1, 3]
    assert (find_range([1, 3, 8, 10, 15], 10)) == [3, 3]
    assert (find_range([1, 3, 8, 10, 15], 12)) == [-1, -1]
    assert (find_range([], 12)) == [-1, -1]


if __name__ == '__main__':
    test()
