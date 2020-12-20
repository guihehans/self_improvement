#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_missing_number.py
@time: 2020/12/4 12:23
@function:
Problem Statement
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""


def find_missing_number(nums):
    """
    using cyclic sort to restore element to their correct position.
    the Time Complexity is O(N)
    in worst case, while loop swap n-1 numbers and then, we move on to next by i+1.
    O(N)+O(N-1)
    and in finding iterating phase, it takes O(N)
    in general, it's O(N)
    the Space complexity is O(1) in place.
    :param nums:
    :return:
    """
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # for sorted array, first i!=nums[i] will be missing number
    for i in range(n):
        if i != nums[i]:
            return i


def finding_missing_number_1(nums):
    """
    this time numbers range from 1-n.
    the array can have duplicates, which means some numbers will be missing. Find all those missing number.
    the difference is there's duplicates, so need to check condition where nums[i]==nums[j]
    :param nums:
    :return:
    """
    missing_number = []
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1  # index of the value represents  need to be -1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # after sort, unmatch ones are results
    for i in range(n):
        if i != nums[i] - 1:
            missing_number.append(i + 1)
    return missing_number


def test():
    inputs = [4, 0, 3, 1]
    assert 2 == find_missing_number(inputs)


def test_1():
    inputs = [2, 3, 1, 8, 2, 3, 5, 1]
    assert [4, 6, 7] == finding_missing_number_1(inputs)


def test_2():
    inputs = [2, 4, 1, 2]
    assert [3] == finding_missing_number_1(inputs)


def test_3():
    inputs = [2, 3, 2, 1]
    assert [4] == finding_missing_number_1(inputs)


if __name__ == '__main__':
    test()
