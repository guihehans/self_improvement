#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: kth_smallest_num_in_M_sorted_list.py
@time: 2021/1/18 16:35
@function:

"""

from heapq import *


def find_Kth_smallest(lists, k):
    number = -1
    min_heap = []
    for i in range(len(lists)):
        sub_list = lists[i]
        if sub_list:
            head_value = sub_list[0]
            heappush(min_heap, (head_value, i, 1))

    while min_heap and k > 0:
        number, total_idx, list_idx = heappop(min_heap)
        k = k - 1
        to_push_list = lists[total_idx]
        if list_idx < len(to_push_list):
            next_val = to_push_list[list_idx]
            heappush(min_heap, (next_val, total_idx, list_idx + 1))

    return number


def test():
    lists = [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
    k = 6
    expected = 6
    assert find_Kth_smallest(lists, k) == expected


def test_1():
    lists = [[5, 8, 9], [1, 7]]
    k = 3
    expected = 7
    assert find_Kth_smallest(lists, k) == expected


if __name__ == '__main__':
    test()
