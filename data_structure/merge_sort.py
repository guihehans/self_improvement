#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: merge_sort.py
@time: 2020/8/6 17:02
@function:

"""
import unittest


def merge_sort(arr):
    """
    divide and conquer.
    1. find the middle point to divide the array into two halves;
        mid=(l+r)/2
    2. call merge_sort for first half.
    3. call merge_sort for second half.
    4. merge the two half.

    :param arr:
    :return:
    """
    if (len(arr)) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """
    the merge function.
    compare left[0] and right[0]. pop the smaller one into result, until all arr empty.

    :param left:
    :param right:
    :return:
    """
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


class TestCase(unittest.TestCase):
    def test(self):
        arr = [2, 5, 1, 8]
        target = [1, 2, 5, 8]
        self.assertTrue(target == merge_sort(arr))

    def test_1(self):
        nums = [2, 11, 7, 15]
        target = [2, 7, 11, 15]
        self.assertTrue(merge_sort(nums) == target)

    def test_2(self):
        nums = [3, 2, 4]
        target = [2, 3, 4]
        self.assertTrue(merge_sort(nums) == target)

    def test_3(self):
        nums = [4, 3, 2, 1, 0, -1]
        target = [-1, 0, 1, 2, 3, 4]
        self.assertTrue(merge_sort(nums) == target)


if __name__ == '__main__':
    unittest.main()
