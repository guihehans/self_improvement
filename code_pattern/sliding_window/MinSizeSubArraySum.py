#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: MinSizeSubArraySum.py
@time: 2020/7/22 11:12
@function:

"""
import math


def smallest_subarray_with_given_sum(s, arr):
    """
    Given an array of positive numbers and a positive number ‘S’,
    find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
    Return 0, if no such subarray exists.

    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

    :param s:
    :param arr:
    :return:
    """
    # solve
    # brutal double loop.
    # start with smallest window, increase the window size until the sum of subarray fit the condition.
    # time complexity O N*N/2.
    # space complexity O (1)

    for i in range(len(arr)):
        window_start = 0
        window_end = i
        for j in range(window_end, len(arr)):
            sum_window = sum(arr[window_start:window_end + 1])
            print(window_start, window_end + 1)
            print(sum_window)
            if sum_window >= s:
                return len(arr[window_start:window_end + 1])
            else:
                window_start = window_start + 1
                window_end = window_end + 1

    return -1


def smallest_subarray_with_given_sum_v1(s, arr):
    """
    improve version
    loop the array in one turn,increase the window size one by one from tail:
    1 .the subarray can be found INSIDE the window by increase the window size until sum>=s.
    2. now we know the subarray COULD be inside the window. record the minimum length when sum>=s.
    3. then try to decrease the window head elements one by one
       if still sum >= s, continue decrease head elements, and record the minimum length when sum>=s..
       else if  sum <s,add the tail to increase window size, until the window reach the array tail.
    4. When the window tail reach the array tail, return the minimum recorded, or return -1 if not found.

    """
    min_len = math.inf
    window_start = 0
    window_end = 0
    while window_end < len(arr):
        if sum(arr[window_start:window_end + 1]) < s:
            window_end = window_end + 1
            pass
        else:
            min_len = min(min_len, len(arr[window_start:window_end + 1]))
            window_start = window_start + 1
    if min_len == math.inf:
        return -1
    else:
        return min_len


if __name__ == '__main__':
    input = [2, 1, 5, 2, 3, 2]
    s = 7
    r = smallest_subarray_with_given_sum_v1(s, input)
    print(r)
