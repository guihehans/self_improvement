#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: MaxPQ.py
@time: 2020/8/26 15:51
@function:

"""
from typing import List


class MaxHeap:
    """
    the maxHeap which each node is larger than it's child.
    """

    def __init__(self, arr):
        self.array = arr
        self.n = len(arr)
        # [n//2,1]->[n//2,0)
        for k in range(self.n // 2, 0, -1):
            self.sink(k, self.n)

    def sort(self):
        """
        the sort function. from collection end,swap the root(largest) to end. restore heapify the
        rest heap until all elements looped and swapped.
        :return:
        """

        k = self.n
        while k > 1:
            self.swap(1, k)
            k -= 1
            self.sink(1, k)
        return self.array

    def sink(self, k, n):
        """
        the sink function to heapify a heap.

        :param k:the start node to sink.
        :param n:the upper bound of heap.
        :return: the heapify heap.
        """
        while 2 * k < n:
            j = 2 * k
            # find larger child
            if j < n and self.less(j, j + 1):
                j += 1
            # if root less than child, swap.
            if not self.less(k, j):
                break
            self.swap(k, j)
            k = j

    def swim(self, k):
        """
        the swim function to heapify a heap at node k.
        at given node, if it's parent less than it, swap it and set focus to parent.
        :param k:
        :return:
        """
        while k > 1 and self.less(k // 2, k):
            self.swap(k, k // 2)
            k = k // 2

    def less(self, i, j):
        return self.array[i - 1] < self.array[j - 1]

    def swap(self, k, j):
        self.array[k - 1], self.array[j - 1] = self.array[j - 1], self.array[k - 1]

    def insert(self, val):
        """
        insert the value to array end, and swim the end node.
        :param val:
        :return:
        """
        self.array.append(val)
        self.n = len(self.array)
        self.swim(self.n)

    def del_max(self):
        """
        del the root node, and swap the end node to root.
        sink until heapify finished.

        :return: max. the max root node's value
        """
        max_val = self.find_root()
        self.swap(1, self.n)
        self.n -= 1
        self.sink(1, self.n)
        del self.array[-1]
        return max_val

    def find_root(self):
        return self.array[0]
