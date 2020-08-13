#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: binary_search_tree.py
@time: 2020/8/13 17:30
@function:

"""

import unittest
from typing import List


class Node:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    a simple binary search tree construct from List[int].
    the list is a binary tree in list structure.e,g. a=[1,3,5,7,10]

    """

    def __init__(self, value_list: List[int]):
        self.root = None
        if value_list:
            for value in value_list:
                self.add_node(value)

    def add_node(self, value: int):
        if not self.root:
            self.root = Node(value)

        else:
            if value < self.root.val:
                self.add_node()
        pass
