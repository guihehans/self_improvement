#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_duplicate.py
@time: 2020/12/4 14:35
@function:
Problem Statement #
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate
but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
"""


def find_duplicate_modify(nums):
    """
    one idea is after cyclic sort, the incorrect number is duplicate.
    the improve version is while swapping, the swapped pair with same value is duplicate.

    :param nums:
    :return:
    """
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:  # swapped with same value, is duplicate
                return nums[i]
        else:
            i += 1
    return -1


# variant problem. find duplicate in O(N) and not modify array
# idea. there will be a cycle, so use fast slow pointers.
# detail in one note.

def find_duplicate(nums):
    fast, slow = nums[0], nums[nums[0]]
    while fast != slow:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # when fast slow meet,
    new_pointer = nums[0]
    while new_pointer != slow:
        new_pointer = nums[new_pointer]
        slow = nums[slow]

    return new_pointer


def test():
    inputs = [1, 4, 4, 3, 2]
    assert 4 == find_duplicate(inputs)


def test_1():
    inputs = [2, 1, 3, 3, 5, 4]
    assert 3 == find_duplicate(inputs)


def test_2():
    inputs = [2, 4, 1, 4, 4]
    assert 4 == find_duplicate(inputs)


if __name__ == '__main__':
    test()
