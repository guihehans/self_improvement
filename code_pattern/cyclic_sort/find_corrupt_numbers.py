#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_corrupt_numbers.py
@time: 2020/12/4 16:49
@function:

"""


def find_corrupt_numbers(nums):
    pair = []
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            pair = [nums[i], i + 1]

    return pair


def test():
    inputs = [3, 1, 2, 5, 2]
    assert [2, 4] == find_corrupt_numbers(inputs)


def test_1():
    inputs = [3, 1, 2, 3, 6, 4]
    assert [3, 5] == find_corrupt_numbers(inputs)


def test_2():
    inputs = [2, 4, 1, 4, 5]
    assert [4, 3] == find_corrupt_numbers(inputs)


if __name__ == '__main__':
    test()
