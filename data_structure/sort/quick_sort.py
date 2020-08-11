#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: quick_sort.py
@time: 2020/8/7 11:19
@function:
quick sort implementation

"""
import unittest


def quick_sort(arr):
    """
    invoke a common recursion function to start.
    :param arr:
    :return:
    """
    return quick_sort_c(arr, left=0, right=len(arr) - 1)


def quick_sort_c(arr, left, right):
    """
    recursion function.

    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left >= right:
        return []
    else:
        q = partition(arr, left, right)
        quick_sort_c(arr, left, q - 1)
        quick_sort_c(arr, q + 1, right)
    return arr


def partition(arr, left, right):
    """
    in-place partition function.
    with pivot set to arr[right], i:j-1 is processed area, j:right-1 is non-processed area.
    each time, if arr[j] <pivot, swap arr[j]q with arr[i], and i++.
    finally, swap the pivot to i.
    return the changed arr and pivot index
    :param arr:
    :param left:
    :param right:
    :return:
    """
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


class TestCase(unittest.TestCase):
    def test(self):
        arr = [2, 5, 1, 8]
        target = [1, 2, 5, 8]
        self.assertTrue(target == quick_sort(arr))

    def test_1(self):
        nums = [2, 11, 7, 15]
        target = [2, 7, 11, 15]
        self.assertTrue(quick_sort(nums) == target)

    def test_2(self):
        nums = [3, 2, 4]
        target = [2, 3, 4]
        self.assertTrue(quick_sort(nums) == target)

    def test_3(self):
        nums = [4, 3, 2, 1, 0, -1]
        target = [-1, 0, 1, 2, 3, 4]
        self.assertTrue(quick_sort(nums) == target)


if __name__ == '__main__':
    unittest.main()
