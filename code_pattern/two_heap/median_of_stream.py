#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: median_of_stream.py
@time: 2020/12/17 16:37
@function:

"""

from data_structure.PQ.MaxPQ import MaxHeap
from data_structure.PQ.MinPQ import MinHeap


class MedianOfAStream:
    """
    one Max_heap to keep smaller n//2 or n//2+1 part, min_heap to keep larger n//2 part.
    median = max_heap.root  if len(max_heap)==n/2+1
    or     = avg(max_heap.root,min_heap.root) if len(max_heap)==len(min_heap)
    """

    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def insert_num(self, num):
        if self.max_heap.n == 0:
            self.max_heap.insert(num)
        else:
            max_root = self.max_heap.find_root()
            if num <= max_root:
                self.max_heap.insert(num)
            else:
                self.min_heap.insert(num)
            # check len, if not balanced, adjust heaps.

            if self.max_heap.n < self.min_heap.n:  # 1. min_heap need to pop
                pop_value = self.min_heap.del_root()
                self.max_heap.insert(pop_value)
            elif self.max_heap.n - self.min_heap.n > 1:  # 2. max_heap need to pop
                pop_value = self.max_heap.del_max()
                self.min_heap.insert(pop_value)
            # else. dont need to adjust

    def find_median(self):
        if self.max_heap.n - 1 == self.min_heap.n:
            return self.max_heap.find_root()
        elif self.max_heap.n == self.min_heap.n:
            return (self.max_heap.find_root() + self.min_heap.find_root()) / 2


def test():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


def test_1():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))


if __name__ == '__main__':
    test()
