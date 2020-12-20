#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_corrupt_numbers.py
@time: 2020/12/4 16:49
@function:

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.

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
    pair = [-1, -1]
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


def test_3():
    inputs = []
    assert [-1, -1] == find_corrupt_numbers(inputs)


def test_4():
    inputs = [3, 2, 1]
    assert [-1, -1] == find_corrupt_numbers(inputs)


if __name__ == '__main__':
    test()
