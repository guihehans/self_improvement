#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: longest_substring_with_k_distinct.py
@time: 2020/7/22 14:41
@function:

    Given a string, find the length of the longest substring in it with no more than K distinct characters.

    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

"""


def longest_substring_with_k_distinct(str, k):
    """
    use sub function to count substring's distinct characters number.
    loop in one turn, until window start and end reach array end:
    1. increase the window size by adding window end,when the distinct characters count <=k
        record the longest length of subarray so far.
    2. when count_distinct_substr >k, decrease window size from head.
    3. return the found longest length of subarray
    Time complexity: O(N*N/2) space complexity: O(N)

    :param str:
    :param k:
    :return:
    """

    def count_distinct_str(string):
        word_count = {}
        for i in range(len(string)):
            word_count[string[i]] = word_count.get(string[i], 0) + 1
        return len(word_count)

    # set window start end. end can be from k-1, since a window of k will have no more than k distinct character.
    window_start, window_end = 0, k - 1
    len_longest = -1
    while window_start < len(str) and window_end < len(str):
        if count_distinct_str(str[window_start:window_end + 1]) <= k:
            len_longest = max(len_longest, len(str[window_start:window_end + 1]))
            if window_end < len(str):
                window_end = window_end + 1
        else:
            window_start = window_start + 1

    return len_longest


def longest_substring_with_k_distinct_v1(str, k):
    """
    improvement:the distinct characters count can be recorded in each slide step. only count the head tail changes.
    Time complexity: O(N)

    :param str:
    :param k:
    :return:
    """

    window_start, window_end = 0, 0
    len_longest = -1
    count_dict = {}
    while window_end < len(str):
        if len(count_dict) <= k:
            count_dict[str[window_end]] = count_dict.get(str[window_end], 0) + 1
            len_longest = max(len_longest, len(str[window_start:window_end]))
            if window_end < len(str):
                window_end = window_end + 1
        else:
            count_dict[str[window_start]] = count_dict[str[window_start]] - 1
            if count_dict[str[window_start]] == 0:
                count_dict.pop(str[window_start])
            window_start = window_start + 1
    return len_longest


if __name__ == '__main__':
    input = "araaci"
    k = 2
    r = longest_substring_with_k_distinct_v1(input, k)
    print(r)
