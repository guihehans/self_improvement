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


def find_Kth_smallest(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) / 2
        count, smaller, larger = count_less_equal_than(mid, matrix, start, end, n)
        if count == k:
            return smaller
        elif count < k:
            start = larger  # search higher value range
        elif count > k:
            end = smaller  # search lower value range

    return start  # in case start == end, when only 1 element


def count_less_equal_than(mid, matrix, start, end, n):
    smaller, larger = start, end
    row, col = n - 1, 0
    count = 0
    while row >= 0 and col < n:
        if matrix[row][col] <= mid:
            count += row + 1
            smaller = max(smaller, matrix[row][col])
            col += 1
        else:
            larger = min(larger, matrix[row][col])
            row -= 1

    return count, smaller, larger


def test():
    matrix = [[2, 6, 8], [3, 7, 10], [5, 8, 11]]
    k = 5
    expected = 7
    assert find_Kth_smallest(matrix, k) == expected


def test_1():
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    expected = 13
    assert find_Kth_smallest(matrix, k) == expected


def test_2():
    matrix = [
        [-5]
    ]
    k = 1
    expected = -5
    assert find_Kth_smallest(matrix, k) == expected


def test_3():
    matrix = [[1, 2], [1, 3]]
    k = 3
    expected = 2
    assert find_Kth_smallest(matrix, k) == expected


if __name__ == '__main__':
    test()
