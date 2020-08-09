#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: selection_sort.py
@time: 2020/8/5 17:39
@function:

selection sort, each step, select smallest to start, then select smallest in remain and append it to tail.

Time O(n^2)
Space O(1)

"""
import unittest


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # pythonic way to swap elements. use a ROW_TWO bytecode instruction to swap top 2 elements in stack
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


class TestCase(unittest.TestCase):
    def test(self):
        arr = [2, 5, 1, 8]
        target = [1, 2, 5, 8]
        self.assertTrue(target == selection_sort(arr))
        nums = [2, 11, 7, 15]
        target = [2, 7, 11, 15]
        self.assertTrue(selection_sort(nums) == target)
        nums = [3, 2, 4]
        target = [2, 3, 4]
        self.assertTrue(selection_sort(nums) == target)
        nums = [4, 3, 2]
        target = [2, 3, 4]
        self.assertTrue(selection_sort(nums) == target)


if __name__ == '__main__':
    unittest.main()
