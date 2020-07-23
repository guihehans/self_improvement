#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: non_repeat_substring.py
@time: 2020/7/23 15:02
@function:

Given a string, find the length of the longest substring which has no repeating characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".


the problem can be described as:
Find the longest sub string, within it each character occurs only once.

"""


def non_repeat_substring(arr):
    window_start = 0
    window_end = 0
    window_end_is_moved = True
    count_dict = {}
    len_longest = -1

    while window_end < len(arr):
        if window_end_is_moved:
            count_dict[arr[window_end]] = count_dict.get(arr[window_end], 0) + 1

        if count_dict.get(arr[window_end], 0) <= 1:
            len_longest = max(len_longest, len(arr[window_start:window_end + 1]))
            window_end = window_end + 1
            window_end_is_moved = True
        else:
            count_dict[arr[window_start]] = count_dict[arr[window_start]] - 1
            if count_dict[arr[window_start]] == 0:
                count_dict.pop(arr[window_start])
            window_start = window_start + 1
            window_end_is_moved = False

        # print(window_start, window_end, len_longest)

    return len_longest


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
