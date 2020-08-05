#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: Subarrays with Product Less than a Target.py
@time: 2020/8/4 15:58
@function:

Given an array with positive numbers and a target number,
find all of its contiguous sub_arrays whose product is less than the target number.

Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Input: [8, 2, 6, 5], target=50
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
Explanation: There are seven contiguous subarrays whose product is less than the target.

"""
from collections import deque


def find_subarrays(arr, target):
    """
    need the sub arrays to be CONTIGUOUS. so no sort.
    with a sliding window, check if window elements' product less than target.
    (by multiply each arr[right], to get an accumulating product.
    if less than, iterate adding arr[left-right] sub array to result.
    if not, left++,begin another round of loop.

    Time complexity:The main for-loop managing the sliding window takes O(N)
    but creating subarrays can take up to O(N^2) in the worst case.
    Therefore overall, our algorithm will take O(N^3).


    :param arr:
    :param target:
    :return:
    """
    result = []

    left = 0
    product = 1

    for right in range(len(arr)):
        # each step adding one right element to product
        product *= arr[right]
        # if product larger than target, loop left ++ and adjust product by divide arr[left
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1

        # now the [left:right]'s product is less than target
        # loop to add arr[right :left] to result.
        tmp_list = deque()
        for i in range(right, left - 1, -1):
            tmp_list.appendleft(arr[i])
            result.append(list(tmp_list))

    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
