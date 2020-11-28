#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_happy_number.py
@time: 2020/11/27 15:08
@function:

"""


def find_happy_number(num):
    num_ = num
    memo = set()
    while True:
        sum = find_sum_sqrt(num_)
        if sum == 1:
            return True
        if sum in memo:
            return False
        num_ = sum
        memo.add(num_)

    return False


def find_sum_sqrt(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += (digit * digit)
        num = num // 10
    return sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


if __name__ == '__main__':
    main()
    print(find_sum_sqrt(12))
