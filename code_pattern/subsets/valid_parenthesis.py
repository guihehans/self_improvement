#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: valid_parenthesis.py
@time: 2020/12/25 10:45
@function:

"""


def generate_valid_parentheses(n):
    result = []

    def backtracking(left, right, cur_set):
        if left == right == 0:
            result.append(cur_set)
            return
        if right > left:
            backtracking(left, right - 1, cur_set + ")")
        if left > 0:
            backtracking(left - 1, right, cur_set + "(")

    backtracking(n, n, "")
    return result


def test_1():
    N = 1
    result = generate_valid_parentheses(N)
    expected = ["()"]
    assert result == expected


def test_2():
    N = 2
    result = generate_valid_parentheses(N)
    expected = ["(())", "()()"]
    assert len(result) == len(expected)
    for r in result:
        assert r in expected


def test_3():
    N = 3
    result = generate_valid_parentheses(N)
    expected = ["((()))", "(()())", "()(())", "(())()", "()()()"]
    assert len(result) == len(expected)
    for r in result:
        assert r in expected


def test_4():
    N = 4
    result = generate_valid_parentheses(N)
    expected = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())",
                "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]

    assert len(result) == len(expected)
    for r in expected:
        assert r in result


if __name__ == '__main__':
    test_1()
