#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: bubble_sort.py
@time: 2020/8/5 16:34
@function:

bubble sort. each loop compare ONLY two contiguous elements. move bigger one backward.
next loop ignore the sorted larger elements, until every elements sorted.

Time O(N^2)
Space O(1)

"""
import unittest


def bubble_sort(arr):
    # outer loop should be len(arr)-1
    for i in range(0, len(arr) - 1):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
    return arr


class TestStudent(unittest.TestCase):
    def test(self):
        nums = [2, 11, 7, 15]
        target = [2, 7, 11, 15]
        self.assertTrue(bubble_sort(nums) == target)
        nums = [3, 2, 4]
        target = [2, 3, 4]
        self.assertTrue(bubble_sort(nums) == target)
        nums = [4, 3, 2]
        target = [2, 3, 4]
        self.assertTrue(bubble_sort(nums) == target)


if __name__ == "__main__":
    unittest.main()
