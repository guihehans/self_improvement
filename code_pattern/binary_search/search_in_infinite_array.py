#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: search_in_infinite_array.py
@time: 2020/12/31 14:17
@function:

"""

import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    start, end = 0, 1
    while True:
        if key < reader.get(start):
            return -1
        elif reader.get(start) <= key <= reader.get(end):
            return binary_search(reader, start, end, key)
        else:
            size = (end - start + 1)
            start = end + 1
            # double the size
            end = end + size << 1


def binary_search(reader: ArrayReader, start, end, key):
    while start <= end:
        mid = start + ((end - start) >> 1)
        mid_value = reader.get(mid)
        if key == mid_value:
            return mid
        elif key < mid_value:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def test():
    arr = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    reader = ArrayReader(arr)
    assert search_in_infinite_array(reader, 16) == 6
    assert search_in_infinite_array(reader, 11) == -1


def test_1():
    arr = [1, 3, 8, 10, 15]
    reader = ArrayReader(arr)
    assert search_in_infinite_array(reader, 15) == 4
    assert search_in_infinite_array(reader, 200) == -1


if __name__ == '__main__':
    test()
