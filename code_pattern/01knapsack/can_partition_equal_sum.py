#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: can_partition_equal_sum.py
@time: 2021/1/28 17:03
@function:

"""


def can_partition(num):
    sum_val = sum(num)
    # check if added items sum equal  to half sum
    return dp(num, 0, sum_val / 2, {})


def dp(num, index, sum, mem):
    # base check
    n = len(num)
    if n == 0:
        return False
    # memo check

    if (index, sum) in mem:
        return mem[(index, sum)]
    # value check
    if sum <= 0:
        return True
    if index >= len(num):
        return False

    if num[index] <= sum:
        if dp(num, index + 1, sum - num[index]):
            mem[(index + 1, sum - num[index])] = True
            return True

    return dp(num, index + 1, sum)


def test():
    arr = [1, 2, 3, 4]
    assert can_partition(arr) is True


def test_1():
    arr = [1, 1, 3, 4, 7]
    assert can_partition(arr) is True


def test_2():
    arr = [2, 3, 4, 6]
    assert can_partition(arr) is False


def test_3():
    arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           99, 97]
    assert can_partition(arr) is True


if __name__ == '__main__':
    test()
