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
        self.root = None
        if value_list:
            for value in value_list:
                node = Node(value)
                self.root = self.add_node(self.root, node)

    def add_node(self, root: Node, new_node: Node):
        """
        recursion function to add a new node to a given node.
        return the modifed root node.
        :param root:
        :param new_node:
        :return: root. return the inserted node.
        """
        if root is None:
            root = new_node
        else:
            if root.val < new_node.val:
                if root.right is None:
                    root.right = new_node
                else:
                    root.right = self.add_node(root.right, new_node)
            else:
                if root.left is None:
                    root.left = new_node
                else:
                    root.left = self.add_node(root.left, new_node)
        return root

    def in_order(self, root: Node):
        if root:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)

    def find(self, node: Node, value: int):
        """
        find the node which equals the given value.
        :param node: the given root node to find
        :param value:
        :return:
        """
        current_node = node
        while current_node:
            if current_node.val == value:
                return current_node
            else:
                if current_node.val < value:
                    return self.find(current_node.right, value)
                else:
                    return self.find(current_node.left, value)
        return "cannot find node in tree"


if __name__ == '__main__':
    arr = [50, 30, 20, 40, 70, 60, 80]
    bst = BinarySearchTree(arr)
    bst.in_order(bst.root)
    node_find=bst.find(bst.root, 40)
    print(node_find)
