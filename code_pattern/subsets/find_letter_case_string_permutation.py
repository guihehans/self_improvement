#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_letter_case_string_permutation.py
@time: 2020/12/24 17:10
@function:

"""


def find_letter_case_string_permutations(str):
    permutations = []

    def backtracking(n, str_list, permutation):
        if n == len(str_list):
            permutations.append(permutation)
            return
        cur_char = str_list[n]

        char_case_list = [cur_char]
        if cur_char.isalpha():
            char_case_list.append(cur_char.swapcase())
        for s in char_case_list:
            backtracking(n + 1, str_list, permutation + s)

    backtracking(0, str, "")
    return permutations


def test():
    test_str = "a1b2"
    result = find_letter_case_string_permutations(test_str)
    expected = ["a1b2", "a1B2", "A1b2", "A1B2"]
    for r in result:
        assert r in expected


def test_1():
    test_str = "3z4"
    result = find_letter_case_string_permutations(test_str)
    expected = ["3z4", "3Z4"]
    for r in result:
        assert r in expected


def test_num():
    test_str = "12345"
    result = find_letter_case_string_permutations(test_str)
    expected = ["12345"]
    for r in result:
        assert r in expected


def test_null():
    test_str = ""
    result = find_letter_case_string_permutations(test_str)
    expected = [""]
    for r in result:
        assert r in expected


if __name__ == '__main__':
    test()
