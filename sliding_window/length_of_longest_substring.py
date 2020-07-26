#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: length_of_longest_substring.py
@time: 2020/7/24 15:09
@function:

Given a string with lowercase letters only,
if you are allowed to replace no more than ‘k’ letters with any letter,
find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

"""


def length_of_longest_substring(str, k):
    """
    1 version
    sliding the window. each time add an element to end,
    check if the window can be made withing replacing k chars.
    if cannot, go back to the next letter from last left char.
    repeat this process until end reach str end.

    Time:O(k*N)  Space:O(k)
    :param str:
    :param k:
    :return:
    """

    window_start = 0
    window_end = 0
    char_index_map = {}
    len_longest = 0
    tmp_k = k

    while window_end < len(str):
        right_char = str[window_end]
        left_char = str[window_start]
        # if right char == left char, the window can be expanded
        if right_char == left_char:
            len_longest = max(len_longest, window_end - window_start + 1)
            char_index_map[right_char] = window_end
        elif right_char != left_char:
            if tmp_k != 0:
                tmp_k = tmp_k - 1
                len_longest = max(len_longest, window_end - window_start + 1)
                char_index_map[right_char] = window_end
            elif tmp_k == 0:
                tmp_k = k
                window_start = char_index_map[left_char] + 1
                window_end = window_start

        window_end = window_end + 1
    return len_longest


def length_of_longest_substring_1(str, k):
    """
    now we count the  max repeat times (max_repeat_times) in a sliding window.
    the max_repeat_times can be get by comparing current value and new frequency map of right char.
    for each char, if the remain char numbers <=k, the substring can be made.
    if >k, then cannot.
    if no substring can be found,shrink the window from head, update the frequency map of removed left char

    With this method, the loop only need to loop N.
    Time: O(N) Space: O(k)

    :param str:
    :param k:
    :return:
    """
    window_start = 0
    max_repeat_time = 0
    frequency_map = {}
    len_longest = 0

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_time = max(max_repeat_time, frequency_map[right_char])

        if window_end - window_start + 1 - max_repeat_time > k:
            left_char = str[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        len_longest = max(len_longest, window_end - window_start + 1)
    return len_longest


def main():
    print(length_of_longest_substring_1("aabccbb", 2))
    print(length_of_longest_substring_1("abbcb", 1))
    print(length_of_longest_substring_1("abccde", 1))


main()
