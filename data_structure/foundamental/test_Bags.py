#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: test_Bags.py
@time: 2020/9/2 14:23
@function:

"""
from data_structure.foundamental.Bag import Bag


class TestBag:
    def test_is_empty(self):
        arr = [1, 2, 3]
        bags = Bag()
        assert bags.is_empty()

    def test_size(self):
        arr = [1, 2, 3]
        bags = Bag()
        bags.add(1)
        assert bags.size() == 1

    def test_add(self):
        arr = [1, 2, 3]
        bags = Bag()
        bags.add(1)
        bags.add(2)
        print(bags)
        assert bags.size() == 2
