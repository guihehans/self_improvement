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

    def __repr__(self):
        return "the node value is {}".format(self.val)


class BinarySearchTree:
    """
    a simple binary search tree construct from List[int].
    the list is a binary tree in list structure.e,g. a=[1,3,5,7,10]

    """

    def __init__(self, value_list: List[int]):
        """
        init the bst from a List[int].
        recursively invoke the add node function until all list members are added.

        :param value_list:
        """
        self.root = None
        if value_list:
            for value in value_list:
                self.add_node(value)

    def add_node(self, value: int):
        """
        recursion function to add a new node to a given node.
        return the modified root node.

        :param value:
        :return:
        """
        if self.root is None:
            self.root = Node(value)
        else:
            current_node = self.root
            tmp_node = Node(value)

            while current_node:
                if value < current_node.val:
                    parent_node = current_node
                    current_node = current_node.left
                    if current_node is None:
                        parent_node.left = tmp_node
                        return True
                else:
                    parent_node = current_node
                    current_node = current_node.right
                    if current_node is None:
                        parent_node.right = tmp_node
                        return True

        return False

    def in_order(self, root: Node):
        if root:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)

    def find(self, value: int):
        """
        find the node which equals the given value.
        refactor to non-recursive version.
        :param value:
        :return:
        """
        current_node = self.root
        while current_node:
            if current_node.val == value:
                return current_node
            else:
                if current_node.val < value:
                    current_node = current_node.right
                else:
                    current_node = current_node.left
        return "cannot find node in tree"

    def delete_node(self):

        pass


if __name__ == '__main__':
    arr = [50, 30, 20, 40, 70, 60, 80]
    bst = BinarySearchTree(arr)
    bst.in_order(bst.root)
    node_find = bst.find(70)

    print(node_find)
