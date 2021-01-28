#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: can_partition_equal_sum.py
@time: 2021/1/28 17:03
@function:

"""


def can_partition(num):
    return dp(num, 0, 0, 0, {})


def dp(num, index, sum1, sum2, mem):
    if index == len(num):
        return sum1 == sum2


    return dp(num, index + 1, sum1 + num[index], sum2) or dp(num, index + 1, sum1, sum2 + num[index])


def test():
    arr = [1, 2, 3, 4]
    assert can_partition(arr) is True


def test_1():
    arr = [1, 1, 3, 4, 7]
    assert can_partition(arr) is True


def test_2():
    arr = [2, 3, 4, 6]
    assert can_partition(arr) is False


if __name__ == '__main__':
    test()
