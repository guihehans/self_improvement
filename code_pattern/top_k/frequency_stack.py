#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: frequency_stack.py
@time: 2021/1/11 17:37
@function:

"""

from heapq import *
import heapq


class FreqStack:

    def __init__(self):
        self.stack = []
        self.max_heap = []
        self.index = {}
        self.n = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x not in self.index:
            self.index[x] = self.n
            heappush(self.max_heap, (-1, x))
            self.n += 1
        else:
            pos = self.index[x]
            freq, item = self.max_heap[pos]
            self.max_heap[pos] = (freq - 1, item)
            heapify(self.max_heap)
            self.index[x] = search_heap(self.max_heap, x)

    def pop(self) -> int:
        pass


def search_heap(max_heap, x):
    for i in range(len(max_heap)):
        freq, item = max_heap[i]
        if x == item:
            return i
    return -1

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
