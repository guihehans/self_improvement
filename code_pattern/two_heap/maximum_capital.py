#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: maximum_capital.py
@time: 2020/12/21 10:00
@function:

"""
from heapq import *


def find_maximum_capital(capitals, profits, numberOfProjects, initialCapital):
    # speed up if all projects can be init. IMPORTANT
    if initialCapital >= max(capitals):
        return initialCapital + sum(nlargest(numberOfProjects, profits))

    capital_min_heap = []
    profit_max_heap = []

    for i in range(len(capitals)):
        heappush(capital_min_heap, (capitals[i], i))

    cur_capital = initialCapital
    for j in range(numberOfProjects):
        # scan and push all projects that satisfy init capital, to max_heap key=profit
        while capital_min_heap and capital_min_heap[0][0] <= cur_capital:
            min_capital, index = heappop(capital_min_heap)
            # max profit heap push. use - to reverse heap to max heap.
            heappush(profit_max_heap, (-profits[index], index))
        # if profit heap empty, no projects satisfy init capital requirement.
        if not profit_max_heap:
            break
        # return the max profit project and add its profit to current capital.
        cur_capital += -heappop(profit_max_heap)[0]

    return cur_capital


def test():
    capitals = [0, 1, 2]
    profits = [1, 2, 3]
    init_capital = 1
    num_projects = 2
    assert find_maximum_capital(capitals, profits, num_projects, init_capital) == 6


def test_1():
    capitals = [0, 1, 2, 3]
    profits = [1, 2, 3, 5]
    init_capital = 0
    num_projects = 3
    assert find_maximum_capital(capitals, profits, num_projects, init_capital) == 8
