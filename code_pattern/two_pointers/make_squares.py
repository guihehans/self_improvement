#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: make_squares.py
@time: 2020/7/31 10:33
@function:

Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]

"""


def make_squares(arr):
    """
    since the start end will give potentially biggest square, the head pointer and tail pointer can be
    set fro start and end, move forward and backward, return the biggest square to result list.

    :param arr:
    :return:
    """
    squares = [0 for i in range(len(arr))]
    head, end = 0, len(arr) - 1
    highest_index = end
    while head <= end:
        add = 0
        if arr[head] * arr[head] > arr[end] * arr[end]:
            add = arr[head] * arr[head]
            head += 1
        else:
            add = arr[end] * arr[end]
            end -= 1
        squares[highest_index] = add
        highest_index -= 1

    return squares


def main():
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))


main()
