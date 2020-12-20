#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: maximum_cpu_load.py
@time: 2020/12/3 13:54
@function:

"""

from heapq import *
from typing import List


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end


def find_max_cpu_load(jobs: List[job]):
    jobs.sort(key=lambda x: x.start)
    min_heap = []
    max_load, current_load = 0, 0
    for job in jobs:
        # remove all ended job in min_heap
        while len(min_heap) > 0 and job.start > min_heap[0].end:
            current_load -= min_heap[0].cpu_load
            heappop(min_heap)
        # push the job in min_heap in min_heap order.
        heappush(min_heap, job)
        current_load += job.cpu_load
        max_load = max(max_load, current_load)

    return max_load


def test():
    assert 7 == find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])


def test_1():
    assert 15 == find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])


def test_2():
    assert 8 == find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])


if __name__ == '__main__':
    test()
