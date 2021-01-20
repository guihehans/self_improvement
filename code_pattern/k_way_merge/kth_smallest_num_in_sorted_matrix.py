#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: kth_smallest_num_in_sorted_matrix.py
@time: 2021/1/18 17:37
@function:

"""

from heapq import *


def find_Kth_smallest(matrix, k):
    number = -1
    m = len(matrix)

    min_heap = []
    for i in range(m):
        row = matrix[i]
        value = row[0]

        heappush(min_heap, (value, i, 1))

    while min_heap:
        number, row_idx, col_idx = heappop(min_heap)
        k = k - 1
        if k == 0:
            break
        if col_idx < m:
            next_value = matrix[row_idx][col_idx]
            heappush(min_heap, (next_value, row_idx, col_idx + 1))

    return number


def test():
    matrix = [[2, 6, 8], [3, 7, 10], [5, 8, 11]]
    k = 5
    expected = 7
    assert find_Kth_smallest(matrix, k) == expected


def test_1():
    matrix = [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
    k = 6
    expected = 6
    assert find_Kth_smallest(matrix, k) == expected


if __name__ == '__main__':
    test()
