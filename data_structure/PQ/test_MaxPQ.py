#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: test_MaxPQ.py
@time: 2020/8/26 16:50
@function:

"""
from data_structure.PQ.MaxPQ import MaxHeap


class TestMaxPQ:
    def test_insert(self):
        array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
        max_heap = MaxHeap(array)
        max_heap.insert("Y")
        assert "Y" == max_heap.find_root()

    def test_del_max(self):
        array = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
        max_heap = MaxHeap(array)
        max_val = max_heap.del_max()
        assert "X" == max_val
