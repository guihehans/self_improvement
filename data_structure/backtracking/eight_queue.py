#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: eight_queue.py
@time: 2020/10/21 10:46
@function:
the eight queues problem is to place 8 queues on 8*8 board, no two queues share same row,column and diagonal.

"""


def print_solution(result, n):
    N = n
    for row in range(N):
        for col in range(N):
            if result[row] == col:
                print('Q', end=' ')
            else:
                print('*', end=' ')
        print()
    print()


def check_state(row, column, result):
    left_up = column - 1
    right_up = column + 1

    # index from last row(row-1) to 0.
    for r in range(row - 1, -1, -1):
        # result r row,column is occupied, return false
        # result diagonal occupied,return false
        if result[r] in [column, left_up, right_up]:
            return False
        left_up -= 1
        right_up += 1
    return True


def n_queen(row, result, n):
    if row == n:
        print(result)
        print_solution(result, n)
    for column in range(n):
        if check_state(row, column, result):
            result[row] = column
            n_queen(row + 1, result, n)


if __name__ == '__main__':
    N = 8
    r_list = [7, 0, 0, 0, 0, 0, 0, 0]
    # defalt ,the 0,0 is placed. check from row 1.
    # so change the first row value we can get all solution.
    n_queen(1, r_list, N)
