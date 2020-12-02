#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: conflicting_appointments.py
@time: 2020/12/2 15:36
@function:

Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
"""
from typing import List


def can_attend_all_appointments(intervals):
    """
    same as find if overlap
    Time O(N*logN)
    Space O(N) for sort
    :param intervals:
    :return:
    """
    n = len(intervals)
    if n < 2:
        return True

    intervals.sort(key=lambda x: x[0])
    start, end = intervals[0][0], intervals[0][1]
    for i in range(1, n):
        # here same a_end and b_start means not conflict
        if intervals[i][0] < end:
            return False
        else:
            start, end = intervals[i][0], intervals[i][1]
    return True


def output_conflict_appointments(intervals: List):
    n = len(intervals)
    if n < 2:
        return True

    intervals.sort(key=lambda x: x[0])
    start, end = intervals[0][0], intervals[0][1]
    for i in range(1, n):
        # here same a_end and b_start means not conflict
        if intervals[i][0] < end:
            print("{} and {} conflict".format([start, end], intervals[i]))
        else:
            start, end = intervals[i][0], intervals[i][1]


def test():
    app = [[1, 4], [2, 5], [7, 9]]
    result = can_attend_all_appointments(app)
    assert result is False


def test_1():
    app = [[6, 7], [2, 4], [8, 12]]
    result = can_attend_all_appointments(app)
    assert result is True


def test_2():
    app = [[4, 5], [2, 3], [3, 6]]
    result = can_attend_all_appointments(app)
    assert result is False


def test_3():
    app = [[1, 4], [4, 5], [7, 9]]
    result = can_attend_all_appointments(app)
    assert result is True


def test_output():
    app = [[4, 5], [2, 3], [3, 6], [5, 7], [7, 8]]
    output_conflict_appointments(app)


if __name__ == '__main__':
    test()
    test_1()
    test_2()
    test_3()
