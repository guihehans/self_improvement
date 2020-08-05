#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: pair_with_targetsum.py
@time: 2020/7/30 14:36
@function:

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

this is the 001 Two sum in leetcode.

"""


def pair_with_targetsum(arr, target_sum):
    """
    since the arr is sorted,
    use two pointers.one head, one tail. compare tmp sum with target sum.
    if tmp_sum > target sum, means the tail element is larger, tail --;
    if tmp_sum < target sum, means the head element is smaller, head ++;
    if equal, return[head,tail]
    Time complexity: O(N); Space complexity: O(1)

    :param arr:
    :param target_sum:
    :return:
    """
    start = 0
    end = len(arr) - 1
    while start < end:
        sum = arr[start] + arr[end]
        # compare the sum to target_sum
        if sum > target_sum:
            end -= 1
        if sum < target_sum:
            start += 1
        if sum == target_sum:
            return [start, end]

    return [-1, -1]


def pair_with_targetsum_1(arr, target_sum):
    """
    the two sum using hash map version
    the idea is literate the array, store each num's index into hashmap.
    the remain =target_sum- num will be found when literate to it's remain.
    Time: O(N) Space: O(N)

    :param arr:
    :param target_sum:
    :return:
    """

    hash_map = {}

    for i in range(len(arr)):
        b = target_sum - arr[i]
        if b in hash_map:
            return [hash_map[b], i]
        hash_map[arr[i]] = i


def main():
    print(pair_with_targetsum_1([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum_1([2, 5, 9, 11], 11))


main()