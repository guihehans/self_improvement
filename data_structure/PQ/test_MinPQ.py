#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: test_MinPQ.py
@time: 2020/8/31 11:13
@function:

"""
from data_structure.PQ.MinPQ import MinHeap


class TestMinPQ:
    def test_sink(self):
        array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
        min_heap = MinHeap(array)
        min_heap.insert("Y")
        assert "A" == min_heap.find_root()

    def test_swim(self):
        array = ["S", "O", "R", "T", "E", "X", "Z", "M", "P", "L", "E"]
        min_heap = MinHeap(array)
        min_heap.insert("A")
        assert "A" == min_heap.find_root()

    def test_greater(self):
        array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
        min_heap = MinHeap(array)
        assert min_heap.greater(2, 1)

    def test_swap(self):
        array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
        min_heap = MinHeap(array)
        min_heap.swap(1, min_heap.n)

        assert "A" == min_heap.array[-1]
