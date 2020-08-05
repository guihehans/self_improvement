#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: length_of_longest_substring_01.py
@time: 2020/7/27 9:25
@function:

Given an array containing 0s and 1s,
if you are allowed to replace no more than ‘k’ 0s with 1s,
find the length of the longest contiguous subarray having all 1s.

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

"""


def length_of_longest_substring(arr, k):
    """
    a window once has fit the condition, the longest len is guaranteed to be no more than the once fitted longest length.
    even in later sliding, the window contains more 0s.

    :param arr:
    :param k:
    :return:
    """
    window_start = 0
    max_repeat_times = 0
    frequency_map = {0: 0, 1: 0}
    len_longest = 0

    for window_end in range(len(arr)):
        right_char = arr[window_end]
        left_char = arr[window_start]
        frequency_map[right_char] += 1
        max_repeat_times = frequency_map[0]

        if max_repeat_times > k:
            frequency_map[left_char] -= 1
            window_start += 1
        len_longest = max(len_longest, window_end - window_start + 1)

    return len_longest


def length_of_longest_substring_1(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        # Current window size is from window_start to window_end, overall we have a maximum of 1s
        # repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
        # and the remaining are 0s which should replace with 1s.
        # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' 0s
        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring([0, 1, 0, 0, 0, 1, 1, 0, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
