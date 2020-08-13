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


def binary_search_find_first(arr: List[int], value: int):
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

        if value < mid_value:
            end = mid - 1
        elif value > mid_value:
            start = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != value:
                return mid
            else:
                end = mid - 1

    return -1


def binary_search_find_last(arr: List[int], value: int):
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

        if value < mid_value:
            end = mid - 1
        elif value > mid_value:
            start = mid + 1
        else:
            if mid == len(arr) - 1 or arr[mid + 1] != value:
                return mid
            else:
                start = mid + 1

    return -1


def binary_search_find_first_ge_than_value(arr: List[int], value: int):
    """
    simple binary search. find the first element which is greater or equal than given value.

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

        if mid_value >= value:
            if mid == 0 or (arr[mid - 1] < value):
                return mid
            else:
                end = mid - 1
        elif mid_value < value:
            start = mid + 1
    return -1


def binary_search_find_first_le_than_value(arr: List[int], value: int):
    """
    simple binary search. find the first element which is less or equal than given value.

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

        if mid_value <= value:
            if mid == len(arr) - 1 or (arr[mid + 1] > value):
                return mid
            else:
                start = mid + 1
        elif mid_value > value:
            end = mid - 1
    return -1


method_list = [binary_search]


class TestCase(unittest.TestCase):

    def test(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 19
        for method in method_list:
            self.assertTrue(2 == method(arr, target))

    def test1(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 0
        for method in method_list:
            self.assertTrue(-1 == method(arr, target))

    def test2(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 9
        for method in method_list:
            self.assertTrue(0 == method(arr, target))

    def test3(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 98
        for method in method_list:
            self.assertTrue(9 == method(arr, target))

    def test4(self):
        arr = [9, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        target = 55
        for method in method_list:
            self.assertTrue(7 == method(arr, target))

    def test_find_first(self):
        arr = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
        target = 8
        index = 5
        method = binary_search_find_first
        self.assertTrue(index == method(arr, target))

    def test_find_last(self):
        arr = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
        target = 8
        index = 7
        method = binary_search_find_last
        self.assertTrue(index == method(arr, target))

    def test_find_first_larger_than_value(self):
        arr = [1, 3, 4, 5, 6, 7, 7.5, 8, 11, 18]
        target = 8
        index = 7
        method = binary_search_find_first_ge_than_value
        self.assertTrue(index == method(arr, target))

    def test_find_first_larger_than_value_1(self):
        arr = [3, 4, 6, 7, 20]
        target = 5
        index = 2
        method = binary_search_find_first_ge_than_value
        self.assertTrue(index == method(arr, target))

    def test_find_first_less_than_value(self):
        arr = [1, 3, 4, 5, 6, 7, 7.5, 8, 11, 18]
        target = 8
        index = 7
        method = binary_search_find_first_le_than_value
        self.assertTrue(index == method(arr, target))

    def test_find_first_less_than_value_1(self):
        arr = [3, 4, 6, 7, 20]
        target = 5
        index = 1
        method = binary_search_find_first_le_than_value
        self.assertTrue(index == method(arr, target))


if __name__ == '__main__':
    unittest.main()
