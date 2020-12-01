#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: merge_intervals.py
@time: 2020/12/1 15:21
@function:

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].

"""

from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    """
    sort the intervals list first. for interval a,b after sorted, a.start<=b.started.
    if b.start<=a.end, a, b overlap. the merged interval end is max(a.end,b.end)
    else, they do not overlap. Since list is sorted, push a to result, make a=b,then repeat.
    after iteration (Time O(N)),need to push the merged/updated interval(start,end).
    Time Complexity: O(logN* N). O(logN*N) for sorting. iterating takes O(N) but smaller than sort.
    Space Complexity: O(N) the result take O(N) space. the sort takes O(N) in general.
    :param intervals: the interval list.
    :return:
    """
    # check len<2 condition
    if len(intervals) < 2:
        return intervals
    # sort using list.sort. key is a function accepting a param and return a key. here use lambda
    # by sorting, it's certain that a.start<= b.start
    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        if intervals[i].start <= end:  # a,b overlaps
            end = max(end, intervals[i].end)
        else:  # a,b not overlaps. since sorted, push a into merged_intervals and make b=a and compare from b.
            merged_intervals.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end

    # add the expanded/updated interval Interval(start, end)
    merged_intervals.append(Interval(start, end))

    return merged_intervals


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


if __name__ == '__main__':
    main()