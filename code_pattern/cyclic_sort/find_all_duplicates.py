#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_all_duplicates.py
@time: 2020/12/4 15:52
@function:
Problem Statement #
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""


def find_all_duplicates(nums):
    duplicateNumbers = []
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
            duplicateNumbers.append(nums[i])

    return duplicateNumbers


def test():
    inputs = [3, 4, 4, 5, 5]
    assert set([4, 5]) == set(find_all_duplicates(inputs))


def test_1():
    inputs = [5, 4, 7, 2, 3, 5, 3]
    assert set([3, 5]) == set(find_all_duplicates(inputs))


def test_2():
    inputs = [2, 4, 1, 4, 1]
    assert set([4, 1]) == set(find_all_duplicates(inputs))


if __name__ == '__main__':
    test()
