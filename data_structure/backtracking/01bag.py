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


if __name__ == '__main__':
    items = [1, 5, 15, 25, 35, 45, 55, 65, 75, 85]
    n = len(items)
    w = 100
    f(0, 0, items, n, w)
    print(maxW)
