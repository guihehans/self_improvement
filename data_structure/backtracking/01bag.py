#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: 01bag.py
@time: 2020/10/23 10:31
@function:

the problem here is to use backtracking to solve 0-1 bag problem.
the problem description is:
1 bag, total weight load is W kg.
n item, each item is in different weight, and cannot be split.
Finding a combination of items to make the bag loads max.

for 3 item, the invoke sequence is like:
0 0 0 update maxW
0 0 1 update maxW
0 1 0 update maxW
0 1 1 update maxW
1 0 0 update maxW
1 0 1 update maxW
1 1 0 update maxW
1 1 1 update maxW

"""
import math

global maxW
maxW = -math.inf
maxV = -math.inf


def f(i, cw, item_list, n, w):
    """

    :param i: the item index to check
    :param cw: current weight
    :param item_list: the item list
    :param n:the number of item in bag
    :param w: max total weight of bag
    :return:
    """
    if cw == w or i == n:
        global maxW
        if cw > maxW:
            maxW = cw
        return
    # here item is not placed, invoke i+1
    f(i + 1, cw, item_list, n, w)
    # here comeback from backtrack, if item i can be add, invoke i+1, cw+item[i]
    if cw + item_list[i] <= w:
        f(i + 1, cw + item_list[i], item_list, n, w)


def max_weight_with_price(i, cw, cv, item_list, value_list, n, w):
    if cw == w or i == n:
        global maxW, maxV
        if cw > maxW:
            maxW = cw
        if cv > maxV:
            maxV = cv
        return
    # check item i not select condition,go to check i+1
    max_weight_with_price(i + 1, cw, cv, item_list, value_list, n, w)
    # return from i+1 to i, now select item i
    if cw + item_list[i] <= w:
        max_weight_with_price(i + 1, cw + item_list[i], cv + value_list[i], item_list, value_list, n, w)


if __name__ == '__main__':
    items = [1, 5, 15, 25, 35, 45, 55, 65, 75, 85]
    values = [0, 5, 5, 25, 15, 5, 55, 65, 75, 85]
    n = len(items)
    w = 100
    # f(0, 0, items, n, w)
    max_weight_with_price(0, 0, 0, items, values, n, w)
    print(maxW)
    print(maxV)
