#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: MinPQ.py
@time: 2020/8/26 15:52
@function:

"""


class MinHeap:
    def __init__(self, arr):
        self.array = arr
        self.n = len(arr)
        # [n//2,1]->[n//2,0)
        for k in range(self.n // 2, 0, -1):
            self.sink(k, self.n)

    def sink(self, k, n):
        """
        the sink function to heapify(sink) a heap.

        :param k:the start node to sink.
        :param n:the upper bound of heap.
        :return: the heapify heap.
        """
        while 2 * k < n:
            j = 2 * k
            # find smaller child, set its index to j
            if j < n and self.greater(j, j + 1):
                j += 1
            # if root greater than child, swap.
            if not self.greater(k, j):
                break
            self.swap(k, j)
            k = j

    def greater(self, i, j):
        return self.array[i - 1] > self.array[j - 1]

    def swap(self, k, j):
        self.array[k - 1], self.array[j - 1] = self.array[j - 1], self.array[k - 1]
