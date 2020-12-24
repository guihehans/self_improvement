#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: n_queen.py
@time: 2020/10/21 10:46
@function:
the eight queues problem is to place 8 queues on 8*8 board, no two queues share same row,column and diagonal.

"""


class NQueen:
    def __init__(self, N):
        self.N = N
        self.result = [0 for _ in range(N)]
        self.solution_cnt = 0

    def print_solution(self):
        N = self.N
        for row in range(N):
            for col in range(N):
                if self.result[row] == col:
                    print('Q', end=' ')
                else:
                    print('*', end=' ')
            print()

        self.solution_cnt += 1
        print("Current solution: {}".format(self.solution_cnt))
        print()

    def is_valid(self, row, column):
        # index from last row(row-1) to 0.
        for cur_row in range(row - 1, -1, -1):
            # result r row,column is occupied, return false
            # result diagonal occupied,return false
            if self.result[cur_row] == column:
                return False
            if abs(self.result[cur_row] - column) == abs(row - cur_row):
                return False
        return True

    def n_queen(self, row):
        if row == self.N:
            print(self.result)
            self.print_solution()

        for column in range(self.N):
            if self.is_valid(row, column):
                self.result[row] = column
                self.n_queen(row + 1)


if __name__ == '__main__':
    N = 8
    n_queen = NQueen(N)
    n_queen.n_queen(0)
