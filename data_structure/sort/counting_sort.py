#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: counting_sort.py
@time: 2020/8/10 14:56
@function:

"""
import unittest
from typing import List


def counting_sort(arr: List[int]):
    if len(arr) < 1:
        return arr
    # 1. init a count_array to count all elements' count.
    # but first, scan to get the max range.
    max_value = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    # init counting array. len is range(0,max_value)
    bucket_len = max_value + 1
    bucket = [0] * bucket_len
    for i in range(len(arr)):
        bucket[arr[i]] += 1
    # accumulating the count, to make each bucket the count is the number of elements which value <element.
    for i in range(1, len(bucket)):
        bucket[i] = bucket[i - 1] + bucket[i]

    tmp_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        # get the current elements index,set the number and count --
        index = bucket[arr[i]] - 1
        tmp_arr[index] = arr[i]
        bucket[arr[i]] -= 1

    return tmp_arr


class TestCase(unittest.TestCase):
    def test(self):
        arr = [2, 5, 1, 8]
        target = [1, 2, 5, 8]
        self.assertTrue(target == counting_sort(arr))

    def test_1(self):
        nums = [2, 11, 7, 15]
        target = [2, 7, 11, 15]
        self.assertTrue(counting_sort(nums) == target)

    def test_2(self):
        nums = [3, 2, 4]
        target = [2, 3, 4]
        self.assertTrue(counting_sort(nums) == target)

    def test_3(self):
        nums = [4, 3, 2]
        target = [2, 3, 4]
        self.assertTrue(counting_sort(nums) == target)


if __name__ == '__main__':
    unittest.main()
    counting_sort("aa")
