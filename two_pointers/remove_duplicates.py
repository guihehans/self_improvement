#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: remove_duplicates.py
@time: 2020/7/30 15:11
@function:

Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space;
after removing the duplicates in-place return the new length of the array.

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

"""


def remove_duplicates(arr):
    """
    since the array is sorted. the repeat elements will only occur after itself.
    didnt fulfill the remove duplicate elements function

    :param arr:
    :return:
    """
    if len(arr) == 1:
        return 1

    start = 0
    end = start + 1
    repeat_time = 0

    while end < len(arr):
        if arr[start] == arr[end]:
            repeat_time += 1
        start += 1
        end += 1

    return len(arr) - repeat_time


def remove_duplicates_1(arr):
    """
    to: 1) find the non repeat length. 2) find the non repeat sub arr
    we should record the next index of non duplicate.
    if repeated, the next_non_duplicate remains, index ++, until we found index element is different with
    non duplicate element. replace it with the next_non_duplicate one, the non_duplicate will be this one,
    so next_non_duplicate ++
    end loop when index reach arr ends.

    Time O(N) Space O(1)
    :param arr:
    :return:
    """

    # index of the next index of non-duplicate element
    next_non_duplicate = 1

    i = 1
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def main():
    print(remove_duplicates_1([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates_1([2, 2, 2, 11]))
    print(remove_duplicates_1([2, 2, 11]))


main()
