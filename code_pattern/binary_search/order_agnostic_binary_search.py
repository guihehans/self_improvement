#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: order_agnostic_binary_search.py
@time: 2020/12/29 17:58
@function:

"""


def binary_search(arr, key):
    # TODO: Write your code here
    return -1


def test():
    assert (binary_search([4, 6, 10], 10)) == 2
    assert (binary_search([1, 2, 3, 4, 5, 6, 7], 5)) == 4
    assert (binary_search([10, 6, 4], 10)) == 0
    assert (binary_search([10, 6, 4], 4)) == 2
    assert (binary_search([10, 6, 4], 7)) == -1


if __name__ == '__main__':
    test()