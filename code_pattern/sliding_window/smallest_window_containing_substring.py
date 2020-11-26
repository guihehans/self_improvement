#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: smallest_window_containing_substring.py
@time: 2020/7/28 13:59
@function:

Given a string and a pattern,
find the smallest substring in the given string which has all the characters of the given pattern.

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.

"""


def find_substring(str1, pattern):
    """
    the idea is, when window expands, find if there's smaller window contains currently found
    character. To achieve this, record each character's latest index, when one character can be removed
    (same as the character at start), change the window start to the smallest char index.
    if all characters are found, return str[start:end+1]

    :param str1:
    :param pattern:
    :return:
    """
    freq_map = {}
    char_index_map = {}

    for c in pattern:
        if c not in freq_map:
            freq_map[c] = 0
        freq_map[c] += 1

    matched = 0
    window_start = 0

    found_first = False
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        left_char = str1[window_start]
        if right_char in freq_map:
            if window_start != window_end and left_char == right_char:
                # the left and right can be swapped,
                # window shrink to the smallest of index of char in window
                char_index_map[right_char] = window_end
                min_index = len(str1)
                for index in char_index_map:
                    min_index = min(min_index, char_index_map[index])
                window_start = min_index
            else:
                if not found_first:
                    found_first = True
                freq_map[right_char] -= 1
                char_index_map[right_char] = max(window_end, char_index_map.get(right_char, -1))
                if freq_map[right_char] == 0:
                    matched += 1
        else:
            if not found_first:
                window_start += 1
        if matched == len(pattern):
            return str1[window_start:window_end + 1]

    return ""


def find_substring_1(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when a useful occurrence of a matched character is going out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start + min_length]




def main_test():
    print(find_substring_1("aabdec", "abc"))
    print(find_substring_1("abdabca", "abc"))
    print(find_substring_1("adcad", "abc"))
    print(find_substring_1("iaibbac", "abc"))


if __name__ == '__main__':
    main_test()
