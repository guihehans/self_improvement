#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_most_intervals_overlap.py
@time: 2020/12/3 10:28
@function:

Input: intervals=[[1,4],[2,5],[9,12],[5,9],[5,12]]
First guest in array arrives at 1 and leaves at 4,
second guest arrives at 2 and leaves at 5, and so on.

Output: 5
There are maximum 3 guests at time 5.


"""
import math
from typing import List
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def find_most_overlap_point(intervals: List[Interval]) -> int:
    intervals.sort(key=lambda x: x.start)
    max_overlap = -1
    point = -1
    min_heap = []
    for interval in intervals:
        # remove all ended interval
        while len(min_heap) > 0 and interval.start > min_heap[0].end:
            heappop(min_heap)
        # push in the interval in min end order
        heappush(min_heap, interval)
        n = len(min_heap)
        if n > max_overlap:
            max_overlap = n
            point = interval.start
    return point


def test():
    intervals = [Interval(1, 4), Interval(2, 5), Interval(9, 12), Interval(5, 9), Interval(5, 12)]
    assert 5 == find_most_overlap_point(intervals)
