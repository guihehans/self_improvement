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
        right_char = arr[window_end]
        left_char = arr[window_start]
        # for first time,read the right char into count dict，view as window end changed
        if window_end_is_moved:
            count_dict[right_char] = count_dict.get(right_char, 0) + 1
        # if the right char occur Once. expand window
        if count_dict.get(right_char, 0) <= 1:
            len_longest = max(len_longest, window_end - window_start + 1)
            window_end = window_end + 1
            window_end_is_moved = True
        # shrink the window,change the each count of char in window
        else:
            count_dict[left_char] = count_dict[left_char] - 1
            if count_dict[left_char] == 0:
                count_dict.pop(left_char)
            window_start = window_start + 1
            window_end_is_moved = False

        # print(window_start, window_end, len_longest)

    return len_longest


def non_repeat_substring_1(str1):
    """
    in fact, the algorithm dont need to care about the detail character's count.
    only the last index of window end should be recorded. when window need to shrink, the window start can jump
    to the current end.

    :param str1:
    :return:
    """
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if right char in char index map, the char could be a read char.
        # compare window start and char_index_map[right_char] to determine if the right char is duplicated right char or
        # old char read.
        if right_char in char_index_map:
            # the start should be max of 1) last right_char index 2)current window start
            window_start = max(window_start, char_index_map[right_char] + 1)
        # save the right char's index into map
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abcdcdefg")))


main()
