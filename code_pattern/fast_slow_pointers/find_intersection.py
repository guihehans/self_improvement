#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_intersection.py
@time: 2020/12/2 13:34
@function:
Problem Statement #
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted
on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""


def merge_my(intervals_a, intervals_b):
    result = []
    len_a = len(intervals_a)
    len_b = len(intervals_b)
    for i in range(len_a):
        for j in range(len_b):
            # if a[i] b[j] not overlap, pass
            if intervals_a[i][1] < intervals_b[j][0] or intervals_a[i][0] > intervals_b[j][1]:
                continue
            else:  # if a[i] b[j] overlap, add their intersection
                c_start = max(intervals_a[i][0], intervals_b[j][0])
                c_end = min(intervals_a[i][1], intervals_b[j][1])
                result.append([c_start, c_end])
    return result


def merge_v1(intervals_a, intervals_b):
    """
    Improve. as a b are all sorted, we can loop ab in order in one loop.
    the overlap: one's start lies within others start and end.
    :param intervals_a:
    :param intervals_b:
    :return:
    """
    result = []
    len_a = len(intervals_a)
    len_b = len(intervals_b)

    i, j = 0, 0
    while i < len_a and j < len_b:
        # a overlap b and b's start lies within a
        a_overlap_b = intervals_a[i][1] >= intervals_b[j][0] >= intervals_a[i][0]
        # b overlap a means a's start lies within a
        b_overlap_a = intervals_b[j][0] <= intervals_a[i][0] <= intervals_b[j][1]

        if a_overlap_b or b_overlap_a:
            c_start = max(intervals_a[i][0], intervals_b[j][0])
            c_end = min(intervals_a[i][1], intervals_b[j][1])
            result.append([c_start, c_end])

        # increase i j by end. the smaller increase first
        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1
    return result


def merge(intervals_a, intervals_b):
    """
    Improve. as a b are all sorted, we can loop ab in order in one loop.
    as long as c_start<c_end, means there;s overlap
    :param intervals_a:
    :param intervals_b:
    :return:
    """
    result = []
    len_a = len(intervals_a)
    len_b = len(intervals_b)

    i, j = 0, 0
    while i < len_a and j < len_b:
        c_start = max(intervals_a[i][0], intervals_b[j][0])
        c_end = min(intervals_a[i][1], intervals_b[j][1])
        if c_start <= c_end:
            result.append([c_start, c_end])

        # increase i j by end. the smaller increase first
        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1
    return result


def test():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


if __name__ == '__main__':
    test()
