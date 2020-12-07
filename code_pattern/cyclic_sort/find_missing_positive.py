#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_missing_positive.py
@time: 2020/12/7 14:21
@function:

Find the Smallest Missing Positive Number (medium) #
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4

Input: nums = [7,8,9,11,12]
Output: 1
"""


def find_first_missing_positive(nums):
    """
    since only returns first missing positive number,
    consider range(1,n) missing problem. ignore all <=0 number and >n numerb.
    1 be on index 0, n be one index n-1. all others just pass.swap the incorrect pairs.
    :param nums:
    :return:
    """

    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        # ignore any numbers <0 or larger than n.
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # return the number not in it's index
    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1


def test():
    inputs = [-3, 1, 5, 4, 2]
    result = find_first_missing_positive(inputs)
    assert 3 == result


def test_1():
    inputs = [3, -2, 0, 1, 2]
    result = find_first_missing_positive(inputs)
    assert 4 == result


def test_2():
    inputs = [3, 2, 5, 1]
    result = find_first_missing_positive(inputs)
    assert 4 == result


def test_3():
    inputs = [8, 7, 10, 11, 12]
    result = find_first_missing_positive(inputs)
    assert 1 == result


if __name__ == '__main__':
    test()
