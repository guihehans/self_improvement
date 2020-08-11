#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: bucket_sort.py
@time: 2020/8/11 10:35
@function:

桶排序
1. 根据数据范围，设立m个大小相同的桶。每个桶代表一定数据范围。
2. 将待排序数据分布于对应数据范围的桶内。
3. 桶内进行排序(O(nlogn))
3. 依照桶的顺序，依次取出数据放回原数组，得到排好序的数组。 排序完成

"""
import math
import unittest


def find_index(val, step, min):
    return (val - min) // step


def bucket_sort(arr):
    # 1. init a bucket, with the (min,max) as bucket range
    min_val, max_value = math.inf, 0
    arr_len = len(arr)
    for i in range(arr_len):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_value:
            max_value = arr[i]

    step = 5
    bucket_len = (max_value - min_val) // step + 1
    bucket = [[] for i in range(bucket_len)]
    for i in range(arr_len):
        i_index = find_index(arr[i], step, min_val)
        bucket[i_index].append(arr[i])

    arr = []
    for i in range(bucket_len):
        bucket[i].sort()
        arr.extend(bucket[i])
    return arr


class TestCase(unittest.TestCase):
    def test(self):
        arr = [2, 5, 1, 8]
        target = [1, 2, 5, 8]
        self.assertTrue(target == bucket_sort(arr))

    def test_1(self):
        nums = [2, 11, 7, 15]
        target = [2, 7, 11, 15]
        self.assertTrue(bucket_sort(nums) == target)

    def test_2(self):
        nums = [3, 2, 4]
        target = [2, 3, 4]
        self.assertTrue(bucket_sort(nums) == target)

    def test_3(self):
        nums = [4, 3, 2]
        target = [2, 3, 4]
        self.assertTrue(bucket_sort(nums) == target)


if __name__ == '__main__':
    unittest.main()
