#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: binary_tree.py
@time: 2020/8/13 14:54
@function:

"""
import unittest
from typing import List


class Node:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    """
    a simple binary tree construct from List[int].
    the list is a binary tree in list structure.e,g. a=[1,3,5,7,10]
    a[0] is the root. a[2*i+1] is left leaf node, a[2*i+2] is right leaf node.

    """
    def __init__(self, value_list: List[int]):
        self.root = None
        if value_list:
            self.root = self.insert_node(value_list, self.root, 0)

    def insert_node(self, value_list: List[int], root: Node, index: int):
        """
        reverse insert node by given index
        :param value_list:
        :param root:L
        :param index:
        :return:
        """
        if index < len(value_list):
            new_node = Node(value_list[index])
            root = new_node

            root.left = self.insert_node(value_list, root.left, 2 * index + 1)
            root.right = self.insert_node(value_list, root.right, 2 * index + 2)

        return root

    def pre_order(self, root: Node):
        if root:
            print("{} ->".format(root.val))
            self.pre_order(root.left)
            self.pre_order(root.right)


if __name__ == '__main__':
    value_list = [1, 3, 5, 7, 10]
    b_tree = BinaryTree(value_list)
    b_tree.pre_order(b_tree.root)
