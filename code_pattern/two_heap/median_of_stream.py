#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: median_of_stream.py
@time: 2020/12/17 16:37
@function:

"""

from heapq import *


class MedianOfAStream:
    """
    one Max_heap to keep smaller n//2 or n//2+1 part, min_heap to keep larger n//2 part.
    median = max_heap.root  if len(max_heap)==n/2+1
    or     = avg(max_heap.root,min_heap.root) if len(max_heap)==len(min_heap)
    """

    def __init__(self):
        # init a max_heap(using - to reverse sort) and a min_heap
        self.min_heap = []
        self.max_heap = []

    def insert_num(self, num):
        if not self.max_heap:
            heappush(self.max_heap, -num)
        else:
            root = - self.max_heap[0]
            if num <= root:
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)
            # adjust the heap size to keep  0<=len(max_heap)-len(min_heap)<=1
            if len(self.max_heap) - len(self.min_heap) > 1:
                value = -heappop(self.max_heap)
                heappush(self.min_heap, value)
            elif len(self.max_heap) < len(self.min_heap):
                value = heappop(self.min_heap)
                heappush(self.max_heap, -value)

    def find_median(self):
        if len(self.max_heap) - len(self.min_heap) == 1:
            return -self.max_heap[0]
        elif len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2


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
