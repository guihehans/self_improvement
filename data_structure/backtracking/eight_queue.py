#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: eight_queue.py
@time: 2020/10/21 10:46
@function:
the eight queues problem is to place 8 queues on 8*8 board, no two queues share same row,column and diagonal.

"""


def print_solution(result):
    N = 8
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

    for r in range(row - 1, -1, -1):
        # result r row,column is occupied, return false
        # result diagonal occupied,return false
        if result[r] in [column, left_up, right_up]:
            return False
        left_up -= 1
        right_up += 1
    return True


def eight_queue(row, result):
    if row == 8:
        print_solution(result)
    for column in range(0, 8):
        if check_state(row, column, result):
            result[row] = column
            eight_queue(row + 1, result)


if __name__ == '__main__':
    r_list = [0] * 8
    eight_queue(1, r_list)
