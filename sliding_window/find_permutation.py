#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_permutation.py
@time: 2020/7/27 11:19
@function:

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

"""


def find_permutation_1(str_param, pattern):
    """
    intuitive method. use a sub function to compare the window content with the pattern.
    One character found, we remove it from pattern copy.
    if the window's characters match all in pattern, the permutation found.
    else, window slide forward.
    the problem is we rely on str.replace and in to check if character all in pattern.
    the str.replace is a O(k) operation.

    Time complexity: O((N-k)*k*k)
    Space complextiy: O(1)

    :param str_param:
    :param pattern:
    :return:
    """
    window_start = 0
    check_result = False

    for window_end in range(len(pattern) - 1, len(str_param)):
        check_result = check_window_in_patter(window_start, window_end, str_param, pattern)
        if check_result:
            return check_result
        else:
            window_start += 1
    return check_result


def check_window_in_patter(start, end, str_param, pattern_):
    for c in range(start, end + 1):
        if str_param[c] in pattern_:
            pattern_ = pattern_.replace(str_param[c], '', 1)
        else:
            return False
    return True


def find_permutation(str_param, pattern):
    """
    improve version. Use Hash map instead of str.replace, to store frequency of character in map.

    Time O((n-k)*k)
    :param str_param:
    :param pattern:
    :return:
    """
    # init all occurrence in pattern.
    frequency_map = {}
    for c in pattern:
        if c not in frequency_map:
            frequency_map[c] = 0
        frequency_map[c] += 1
    window_start = 0
    check_result = False

    for window_end in range(len(pattern) - 1, len(str_param)):
        check_result = check_window_in_pattern(window_start, window_end, str_param, frequency_map)
        if check_result:
            return check_result
        else:
            window_start += 1
    return check_result


def check_window_in_pattern(start, end, str_param, freq_map):
    frequency_map = freq_map.copy()
    for c in range(start, end + 1):
        if str_param[c] in frequency_map:
            frequency_map[str_param[c]] -= 1
            if frequency_map[str_param[c]] == 0:
                frequency_map.pop(str_param[c])
        else:
            return False
    return True


def find_permutation(str1, pattern):
    """
    finish the query in ONE loop. The trick is use a matched to represent how many character we found in pattern
    if freq[char] ==0. when window expands, this number could be less than zero.but when window shrink, the frequency will
    increase again. once matched == len(patter), all char matched== return true.
    :param str1:
    :param pattern:
    :return:
    """

    # init all occurrence in pattern.
    frequency_map = {}
    for c in pattern:
        if c not in frequency_map:
            frequency_map[c] = 0
        frequency_map[c] += 1
    window_start = 0
    matched = 0

    for window_end in range(len(str1)):
        if str1[window_end] in frequency_map:
            frequency_map[str1[window_end]] -= 1
            if frequency_map[str1[window_end]] == 0:
                matched += 1

        if matched == len(frequency_map):
            return True

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in frequency_map:
                frequency_map[left_char] += 1
                if frequency_map[left_char] > 0:
                    matched -= 1

    return False


def test():
    print(find_permutation("oidbcaf", "abc"))
    print(find_permutation("odicf", "dc"))
    print(find_permutation("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation("aaacb", "abc"))


if __name__ == '__main__':
    test()
