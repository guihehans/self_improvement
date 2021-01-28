#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: 01knapsack.py
@time: 2021/1/27 15:05
@function:

"""
from typing import List


def solve_knapsack_dp(profits: List[int], weights: List[int], capacity: int) -> int:
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


class Knapsack:

    def __init__(self, profits=[], weights=[], capacity=0):
        self.capacity = capacity
        self.weights = weights
        self.profits = profits
        self.n = len(profits)
        self.max_profit = 0

    def solve_knapsack(self, profits: List[int], weights: List[int], capacity: int) -> int:
        self.__init__(profits, weights, capacity)
        self.backtracking(0, 0, 0)  # invoke from item0, current_weight=0, and current_profit=0
        return self.max_profit

    def backtracking(self, index: int, cur_weight, cur_profit):
        if cur_weight == self.capacity or index == self.n:
            if cur_profit > self.max_profit:  # the max_profit update only when reach bottom.
                self.max_profit = cur_profit
            return

        self.backtracking(index + 1, cur_weight, cur_profit)
        if cur_weight + self.weights[index] <= self.capacity:  # 剪枝 pruning
            self.backtracking(index + 1, cur_weight + self.weights[index], cur_profit + self.profits[index])


def test():
    k = Knapsack()
    print(k.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(k.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(k.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(k.solve_knapsack([3, 4, 8, 9,6], [2, 2, 4, 6,3], 9))
    print(solve_knapsack_dp([3, 4, 8, 9,6], [2, 2, 4, 6,3], 9))

if __name__ == '__main__':
    test()
