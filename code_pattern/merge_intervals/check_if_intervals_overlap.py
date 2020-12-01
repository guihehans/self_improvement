#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: check_if_intervals_overlap.py
@time: 2020/12/1 16:24
@function:

Problem : Given a set of intervals, find out if any two intervals overlap.

Example:

Intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap

"""
from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[{},{}]".format(self.start, self.end))


def check_if_overlap(intervals: List[Interval]) -> bool:
    """
    check if the List[intervals] elements, any two overlap.
    True for overlap, False for not overlap.

    :param intervals:
    :return:
    """
    if len(intervals) < 2:
        return False
    intervals.sort(key=lambda interval: interval.start)
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        if intervals[i].start <= end:  # overlap
            return True
        else:
            start = intervals[i].start
            end = intervals[i].end

    return False


def test():
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    result = check_if_overlap(intervals)
    assert result is True


def test_1():
    intervals = [Interval(1, 4)]
    result = check_if_overlap(intervals)
    assert result is False


def test_2():
    intervals = []
    result = check_if_overlap(intervals)
    assert result is False


def test_3():
    intervals = [Interval(1, 2), Interval(3, 4), Interval(7, 9)]
    result = check_if_overlap(intervals)
    assert result is False


