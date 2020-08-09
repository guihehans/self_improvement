#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: shell_sort.py
@time: 2020/8/6 15:44
@function:

"""
import unittest


def shell_sort(arr):
    n = len(arr)
    # 初始步長
    gap = n // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            # insert sort. the temp is the card. the sequence is [i-gap,i-gap-gap,...]
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = gap // 2

    return arr


class TestCase(unittest.TestCase):
    def test(self):
        arr = [2, 5, 1, 8]
        target = [1, 2, 5, 8]
        self.assertTrue(target == shell_sort(arr))

    def test_1(self):
        nums = [2, 11, 7, 15]
        target = [2, 7, 11, 15]
        self.assertTrue(shell_sort(nums) == target)

    def test_2(self):
        nums = [3, 2, 4]
        target = [2, 3, 4]
        self.assertTrue(shell_sort(nums) == target)

    def test_3(self):
        nums = [4, 3, 2, 1, 0, -1]
        target = [-1, 0, 1, 2, 3, 4]
        self.assertTrue(shell_sort(nums) == target)


if __name__ == '__main__':
    unittest.main()
