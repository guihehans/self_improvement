#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: insert_interval.py
@time: 2020/12/1 17:00
@function:
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position
and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""


def insert(intervals, new_interval):
    if len(intervals) < 1:
        return [new_interval]

    merged = []
    # 1. insert new_interval at correct index
    # 2. iterating the list, merge the overlapped intervals.
    insert_index = 0
    for i in range(len(intervals)):
        a = intervals[i]
        b = new_interval
        if b[1] <= a[1]:
            insert_index = 0
            break
        elif a[1] <= b[0]:
            insert_index = i
            break
        elif True:
            break

    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
