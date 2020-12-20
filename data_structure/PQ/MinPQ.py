#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: MinPQ.py
@time: 2020/8/26 15:52
@function:

the minHeap heapify can ensure the largest element to be sink to the heap bottom, make the Top k element stay in minheap
so it's useful for top-k problem.
"""


class MinHeap:
    """
    the minHeap which each node is less than it's child.
    the low level is array and its index is from 0-n.
    the top level index k is from 1-n+1

    """

    def __init__(self, arr=[]):
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

    def swim(self, k):
        """
        the swim function to heapify.

        :param k:
        :return:
        """
        while k > 1 and self.greater(k // 2, k):
            self.swap(k // 2, k)
            k = k // 2

    def insert(self, val):
        """
        insert a val at end of heap. swim the node to heapify

        :param val:
        :return:
        """
        self.array.append(val)
        self.n = len(self.array)
        self.swim(self.n)

    def del_root(self) -> int:
        """
        delete the root node which is minimum.
        swap the end node to root, delete the end node, and sink down to heapify.

        :return:
        """
        min_val = self.find_root()
        self.swap(1, self.n)
        self.n -= 1
        self.sink(1, self.n)
        del self.array[-1]
        return min_val

    def find_root(self):
        return self.array[0]

    def greater(self, i, j):
        return self.array[i - 1] > self.array[j - 1]

    def swap(self, k, j):
        self.array[k - 1], self.array[j - 1] = self.array[j - 1], self.array[k - 1]
