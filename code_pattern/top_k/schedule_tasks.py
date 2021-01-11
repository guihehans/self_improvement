#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: schedule_tasks.py
@time: 2021/1/11 16:36
@function:

"""

from heapq import *
from typing import List


def schedule_tasks(tasks, K):
    if K == 0:
        return len(tasks)

    freq_map = {}
    for char in tasks:
        freq_map[char] = freq_map.get(char, 0) + 1

    max_heap = []
    for char, freq in freq_map.items():
        heappush(max_heap, (-freq, char))

    intervalCount = 0

    while max_heap:
        n = K + 1
        tmp = []
        while n > 0 and max_heap:
            freq, char = heappop(max_heap)
            intervalCount += 1
            if -freq > 1:
                tmp.append((freq + 1, char))
            n -= 1

        for freq, char in tmp:
            heappush(max_heap, (freq, char))

        if max_heap:
            intervalCount += n

    return intervalCount


def test():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    expected = 8
    assert schedule_tasks(tasks, n) == expected


def test_1():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    expected = 6
    assert schedule_tasks(tasks, n) == expected


def test_2():
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    expected = 16
    assert schedule_tasks(tasks, n) == expected


def test_2():
    tasks = ["a", "b", "a"]
    n = 3
    expected = 5
    assert schedule_tasks(tasks, n) == expected


if __name__ == '__main__':
    test()
