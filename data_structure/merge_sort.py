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
    pass


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
