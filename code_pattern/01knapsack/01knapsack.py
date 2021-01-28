#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: 01knapsack.py
@time: 2021/1/27 15:05
@function:

"""
from typing import List


def solve_knapsack_dp(profits: List[int], weights: List[int], capacity: int):
    states = [-1 for _ in range(capacity + 1)]
    n = len(weights)
    assert n == len(profits)
    # update item 0
    states[0] = 0
    if weights[0] <= capacity:
        states[weights[0]] = profits[0]

    for i in range(1, n):
        # not picking no need to update.so only picking item[i] will be considered.
        # reverse traverse so wont effect states check
        # if picking weight[i], the capacity>weight[i] +weight[i] will exceeding capacity, so pass.
        # so range(capacity - weights[i], -1, -1)
        for j in range(capacity - weights[i], -1, -1):
            if states[j] >= 0:  # value not -1.
                if states[j] + profits[i] > states[j + weights[i]]:
                    states[j + weights[i]] = states[j] + profits[i]

    return max(states)


def test():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


if __name__ == '__main__':
    test()
