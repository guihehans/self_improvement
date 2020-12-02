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


def insert_my(intervals, new_interval):
    if len(intervals) < 1:
        return [new_interval]

    merged = []
    # 1. insert new_interval at correct index
    # 2. iterating the list, merge the overlapped intervals.
    for i in range(len(intervals)):
        if new_interval[0] <= intervals[i][0]:
            intervals.insert(i, new_interval)
        elif i == len(intervals) - 1:
            intervals.append(new_interval)

    start, end = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        next_start, next_end = intervals[i][0], intervals[i][1]
        if next_start <= end:  # overlap, merge end
            end = max(end, next_end)
        else:  # no overlap, push current [start,end] and make interval a=b. loop to compare with next interval
            merged.append([start, end])
            start = next_start
            end = next_end
    merged.append([start, end])

    return merged


def insert(intervals, new_interval):
    if len(intervals) < 1:
        return [new_interval]

    merged = []
    n = len(intervals)  # use n to avoid counting cost
    # One loop idea.
    # 1. push all intervals a that ends before b start
    i = 0
    while i < n and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1
    # 2. now merge the intervals that overlap with new_interval b
    # overlaps condition: a.start<=b.end
    #    the new_interval start =min(a_start,b_start) end=max(a_end,b_end)
    #   continue merge all a and b until no overlap
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    # push the final merged interval
    merged.append(new_interval)

    # 3. append rest non overlap interval a that a.start> b.ends
    while i < n and intervals[i][0] > new_interval[1]:
        merged.append(intervals[i])
        i += 1

    return merged


def test():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


if __name__ == '__main__':
    test()
