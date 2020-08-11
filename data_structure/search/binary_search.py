#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: binary_search.py
@time: 2020/8/11 16:23
@function:

"""
import math
import unittest
from typing import List


def binary_search(arr: List[int], value: int):
    """
    simple binary search. assume that no element is repeated.

    :param arr:List[int]. the array to search
    :param value:int. the value to search.
    :return: index: int. return the index of found element or -1 if not found.
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        # to avoid start+end overflow and bit operate is faster, use current start+((end-start)>>1)
        # which is start+(end-start)/2
        mid = start + ((end - start) >> 1)
        mid_value = arr[mid]
        if value == mid_value:
            return mid
        elif value < mid_value:
            end = mid - 1
        else:
            start = mid + 1

    return -1


class TestCase(unittest.TestCase):
    def test(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 19
        self.assertTrue(2 == binary_search(arr, target))

    def test1(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 0
        self.assertTrue(-1 == binary_search(arr, target))

    def test2(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 9
        self.assertTrue(0 == binary_search(arr, target))

    def test3(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 98
        self.assertTrue(9 == binary_search(arr, target))

    def test4(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 55
        self.assertTrue(7 == binary_search(arr, target))


if __name__ == '__main__':
    unittest.main()
