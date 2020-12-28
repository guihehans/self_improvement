#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: evaluate_expression.py
@time: 2020/12/28 10:42
@function:

"""


def diff_ways_to_evaluate_expression(input):
    if input.isdigit():
        return [int(input)]

    result = []
    for i, char in enumerate(input):
        if char in ["+", "-", "*"]:
            left = diff_ways_to_evaluate_expression(input[:i])
            right = diff_ways_to_evaluate_expression(input[i + 1:])
            for l in left:
                for r in right:
                    result.append(cal_expression(l, r, char))
    return result


def cal_expression(op1, op2, operator):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    else:
        return -1


def test():
    expression = "2-1-1"
    result = diff_ways_to_evaluate_expression(expression)
    expected = [0, 2]
    for r in expected:
        assert r in result
    assert len(result) == len(expected)


def test_1():
    expression = "2*3-4*5"
    result = diff_ways_to_evaluate_expression(expression)
    expected = [-34, -14, -10, -10, 10]
    for r in expected:
        assert r in result
    assert len(result) == len(expected)


if __name__ == '__main__':
    test()
