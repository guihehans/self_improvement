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

from data_structure.PQ.MaxPQ import MaxHeap
from data_structure.PQ.MinPQ import MinHeap


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
    min_heap = MinHeap(arr[:k])
    for i in range(k, len(arr)):
        if arr[i] > min_heap.array[0]:
            min_heap.array[0] = arr[i]
            min_heap.sink(1, k)

    return min_heap.array


def find_median(arr):
    """
    find the median(can be expand to k-percentile)
    store median in v.
    init and maintain a max-heap to store elements less than v;
    init and maintain a min-heap to store elements larger than v;
    iterate tha collection, each time insert a new element, and compare it with v,
    to decide which heap to insert.

    :param arr:
    :return:
    """
    for i in range(len(arr)):
        pass


if __name__ == '__main__':
    array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
    heap = MaxHeap(array)
    print(heap.array)
    heap.sort()
    print(heap.array)
    array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
    print(top_k(4, array))
