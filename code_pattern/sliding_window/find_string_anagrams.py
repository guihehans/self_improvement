#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_string_anagrams.py
@time: 2020/7/28 10:12
@function:

Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

"""


def find_string_anagrams(str_, pattern):
    result_indexes = []

    # init the freq map of pattern
    frequency_map = {}
    for c in pattern:
        if c not in frequency_map:
            frequency_map[c] = 0
        frequency_map[c] += 1

    # init a matched variable
    matched = 0
    window_start = 0
    for window_end in range(len(str_)):
        if str_[window_end] in frequency_map:
            frequency_map[str_[window_end]] -= 1
            if frequency_map[str_[window_end]] == 0:
                matched += 1

        if matched == len(pattern):
            result_indexes.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str_[window_start]
            window_start += 1
            if left_char in frequency_map:
                frequency_map[left_char] += 1
                if frequency_map[left_char] > 0:
                    matched -= 1

    return result_indexes


def main_test():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))
    print(find_string_anagrams("abbcabceabc", "abc"))


if __name__ == '__main__':
    main_test()
