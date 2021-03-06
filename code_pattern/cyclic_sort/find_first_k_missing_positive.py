#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_first_k_missing_positive.py
@time: 2020/12/7 16:21
@function:

Find the First K Missing Positive Numbers (hard)
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
"""


def find_first_k_missing_positive_my(nums, k):
    """

    :param nums:
    :param k: the k missing positive need to find.
    :return:
    """
    i, n = 0, len(nums)
    if n < 1:
        return []

    min_num = min(filter(lambda x: x >= 0, nums))

    while i < n:
        j = nums[i] - min_num
        if 0 < nums[i] <= n + min_num and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # use two pointer i,j to compare range(1,n+k) with sorted nums. when element in range(1,n+k)
    # doesnt match nums[i], add j to result. or when visit all nums, still missing, add j one by one .
    i, j = 0, 1
    result = []
    while k > 0:
        if i < n and j <= n + k:
            if j != nums[i]:
                result.append(j)
                k -= 1
                j += 1
            else:
                j += 1
                i += 1
        else:
            result.append(j)
            j += 1
            k -= 1

    return result


def find_first_k_missing_positive(nums, k):
    """
    same idea as find first missing positive,
    the difference is
    :param nums:
    :param k:
    :return:
    """
    i, n = 0, len(nums)
    # cyclic sort nums. in range[1,n]
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # iterate nums, add missing and wrong placed numbers
    missing_nums = []
    extra_set = set()
    for i in range(0, n):
        if k > 0 and nums[i] != i + 1:
            missing_nums.append(i + 1)
            k -= 1
            if nums[i] > 0:
                extra_set.add(nums[i])

    # if still k elements not found,from i=n+1, add it if not see before
    i = n
    while k > 0:
        i += 1
        if i not in extra_set:
            missing_nums.append(i)
            k -= 1

    return missing_nums


def test():
    inputs = [3, -1, 4, 5, 5]
    k = 3
    result = find_first_k_missing_positive(inputs, k)
    assert [1, 2, 6] == result


def test_1():
    inputs = [2, 3, 4]
    k = 3
    result = find_first_k_missing_positive(inputs, k)
    assert [1, 5, 6] == result


def test_2():
    inputs = [-2, -3, 4]
    k = 2
    result = find_first_k_missing_positive(inputs, k)
    assert [1, 2] == result


def test_3():
    inputs = []
    k = 0
    result = find_first_k_missing_positive(inputs, k)
    assert [] == result


if __name__ == '__main__':
    test()
