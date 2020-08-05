#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: search_triplets.py
@time: 2020/7/31 14:45
@function:

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

"""


def search_for_pair(arr, i, result_list):
    """
    sub function to find unique triplets.
    since there may be 1+ triplets in one search, the result add as parameter
    is simpler than return.

    Sorting the array will take O(N * logN).
    The searchPair() function will take O(N).
    As we are calling searchPair() for every number in the input array,
    this means that overall searchTriplets() will take O(N * logN + N^2),
    which is asymptotically equivalent to O(N^2).
    :param arr:
    :param i:
    :param result_list:
    :return:
    """
    cur = arr[i]
    to_find_sum = - cur
    left = i + 1
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == to_find_sum:
            result_list.append([cur, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif arr[left] + arr[right] < to_find_sum:
            left += 1
        else:
            right -= 1


def search_triplets(arr):
    result_list = []
    arr.sort()

    for i in range(len(arr)):
        # skip duplicate elements
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_for_pair(arr, i, result_list)

    return result_list


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
