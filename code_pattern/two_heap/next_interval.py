#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: next_interval.py
@time: 2020/12/21 17:52
@function:

"""

from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    result = []
    max_heap = []
    for i in range(len(intervals)):
        interval = intervals[i]
        heappush(max_heap, (-interval.start, i))

    return result


def main():
    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
