#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: k_closest_2D_points.py
@time: 2021/1/7 11:17
@function:

"""
import math
from typing import List
from heapq import *


def k_closest(points: List[List[int]], k) -> List[List[int]]:
    max_heap = []
    for i in range(len(points)):
        if i < k:
            heappush(max_heap, (-eu_dist_to_zero(points[i]), points[i]))
        else:
            cur_dist = eu_dist_to_zero(points[i])
            if cur_dist < -max_heap[0][0]:
                heappushpop(max_heap, (-cur_dist, points[i]))

    result_list = []
    for i in range(k):
        dist, point = max_heap[i]
        result_list.append(point)
    return result_list


def eu_dist_to_zero(point_x: List[int]):
    eu_dist = point_x[0] ** 2 + point_x[1] ** 2
    return eu_dist


def test():
    points = [[1, 3], [-2, 2]]
    k = 1
    expected = [[-2, 2]]
    result = k_closest(points, k)
    assert len(result) == len(expected)
    for item in expected:
        assert item in result


def test_1():
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    expected = [[3, 3], [-2, 4]]
    result = k_closest(points, k)
    assert len(result) == len(expected)
    for item in expected:
        assert item in result


if __name__ == '__main__':
    test()
