#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: generate_abbreviations.py
@time: 2020/12/25 16:30
@function:

"""


def generate_generalized_abbreviation(word):
    result = []

    def backtracking(n, word, path):
        if n == len(word):
            result.append(path)
            return

        current_char = word[n]
        new_path = path + current_char
        backtracking(n + 1, word, new_path)

        add_path = path + "1"
        if len(path) >= 1 and path[-1].isdigit():
            add_path = path[:-1] + str(int(path[-1]) + 1)
        backtracking(n + 1, word, add_path)

    backtracking(0, word, "")
    return result


def test():
    word = "a"
    result = generate_generalized_abbreviation(word)
    expected = ["a", "1"]

    assert len(result) == len(expected)
    for r in expected:
        assert r in result


def test_4():
    word = "word"
    result = generate_generalized_abbreviation(word)
    print(result)
    expected = ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d",
                "w3", "4"]

    assert len(result) == len(expected)
    for r in expected:
        assert r in result


if __name__ == '__main__':
    test()
