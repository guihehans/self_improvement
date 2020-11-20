#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: knapsack.py
@time: 2020/11/20 17:20
@function:

"""


def knapsack_2d(item, n, w):
    """
    the knapsack using 2d state array version.
    :param item: the item weight array
    :param n: numbers of items.
    :param w: the knapsack's max capacity
    :return: the max weight under w.
    """

    states = [[False for i in range(w + 1)] for j in range(n)]
    # init first states[0] row. including item[i]
    states[0][0] = True
    if item[0] < w:
        states[0][item[0]] = True

    # i is from 1(2nd row)
    for i in range(1, n):
        for j in range(0, w + 1):  # not picking states
            if states[i - 1][j]:
                states[i][j] = True
        for j in range(0, w + 1 - item[i]):  # picking item[i] states
            if states[i - 1][j]:
                states[i][j + item[i]] = True

    # return max states which is right bottom one
    for i in range(w, -1, -1):
        if states[n - 1][i]:
            return i
    return 0


def knapsack_1d_arr(item, n, w):
    """
    1d array version
    Time O(n*w)
    Space O(w)
    :param item:
    :param n:
    :param w:
    :return:
    """
    # init states
    states = [False for i in range(w + 1)]
    # init the 0 stage
    states[0] = True
    if item[0] < w:
        states[item[0]] = True
    # dp each stage
    for i in range(1, n):
        for j in range(0, w + 1):  # not picking item[i]
            if states[j]:
                states[j] = True
        for j in range(w - item[i], -1, -1):  # picking item[i].
            # reverse j so adding item[i] will not leading endless loop
            if states[j]:
                states[j + item[i]] = True

    # return max weight
    for i in range(w, -1, -1):
        if states[i]:
            return i
    return 0


def knapsack_value(item, value, n, w):
    return


def test_case():
    arr = [2, 2, 4, 6, 3]
    n = len(arr)
    w = 9
    value = knapsack_2d(arr, n, w)
    print(value)
    assert value == 9


def test_case_1():
    arr = [2, 2, 4, 6, 3]
    n = len(arr)
    w = 9
    value = knapsack_1d_arr(arr, n, w)
    print(value)
    assert value == 9


if __name__ == '__main__':
    test_case()
    test_case_1()
