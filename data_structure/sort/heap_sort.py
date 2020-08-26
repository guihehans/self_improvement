#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: heap_sort.py
@time: 2020/8/10 9:49
@function:

arr=S O R T E X A M P L E
Heap.sort(arr)
A E E L M O P R S T X

"""
from typing import List


class Heap:
    def __init__(self, arr):
        self.array = arr
        self.n = len(arr)
        # [n//2,1]->[n//2,0)
        for k in range(self.n // 2, 0, -1):
            self.sink(k, self.n)

    def sort(self):
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

    def less(self, i, j):
        return self.array[i - 1] < self.array[j - 1]

    def swap(self, k, j):
        self.array[k - 1], self.array[j - 1] = self.array[j - 1], self.array[k - 1]


class MinHeap:
    def __init__(self, arr):
        self.array = arr
        self.n = len(arr)
        # [n//2,1]->[n//2,0)
        for k in range(self.n // 2, 0, -1):
            self.sink(k, self.n)

    def sink(self, k, n):
        """
        the sink function to heapify a heap.

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


def top_k(k, arr):
    """
    return the top k largest elements of given array.
    init a min-heap of k size,push the elements into the heap.
    if current node is larger than root, insert the node to root and sink;
    else do nothing.
    after all elements pushed, the top k elements is stored in heap.
    time complexity: O(nlogk)~ O(n)
    space O(1)

    :param k:
    :param arr: the given arr.
    :return:
    """
    minHeap = MinHeap(arr[:k])
    print(minHeap.array)
    for i in range(k, len(arr)):
        if arr[i] > minHeap.array[0]:
            minHeap.array[0] = arr[i]
            minHeap.sink(1, k)

    print(minHeap.array)


if __name__ == '__main__':
    array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
    heap = Heap(array)
    print(heap.array)
    heap.sort()
    print(heap.array)
    array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
    top_k(5, array)
