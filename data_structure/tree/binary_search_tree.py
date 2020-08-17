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
        if: check if root node is empty. if true, insert to root.
        else:root not empty
            while current node is not None, loop:
                compare the value with current node's value.
                if value< cur.val,
                    parent is current node
                    current node to left child.
                    if current node(child) None, insert and return
                else:
                    parent is current node
                    current node to right child.
                    if current node(child) None,insert and return
        finish.

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

    def delete_node(self, value: int):
        """
        the method to delete node which's val equals given value
        1. find the node. if not found, return.
        2. the node to delete, can be categorized into following:
            2.1. no child. delete directly.
            2.2. one child. swap the child with the node.
            2.3 two child. swap the most left child in right child tree(minimum child).

        in code, the 2.1 2.2 can be summarized as, parent node ->child node(if no child, none).
        it's infact the operation to delete current node.
        so the 2.3 can be summarized as ,find to delete node and its parent.
        then link parent node ->child node in total.

        :param value:
        :return:
        """
        current_node: Node = self.root
        parent_node: Node = None
        while current_node and current_node.val != value:
            parent_node = current_node
            if current_node.val < value:
                current_node = current_node.right
            else:
                current_node = current_node.left

        if current_node is None:
            return None

        # 1. two child
        if current_node.left and current_node.right:
            min_node: Node = current_node.right
            min_node_parent: Node = current_node
            while min_node.left:
                min_node_parent = min_node
                min_node = min_node.left
            # set current node value.
            current_node.val = min_node.val
            current_node = min_node
            parent_node = min_node_parent

        child: Node = None
        if current_node.left:
            child = current_node.left
        elif current_node.right:
            child = current_node.right
        else:
            child = None

        if parent_node is None:
            self.root = child
        elif parent_node.left == current_node:
            parent_node.left = child
        else:
            parent_node.right = child


if __name__ == '__main__':
    arr = [50, 30, 20, 40, 70, 60, 80]
    bst = BinarySearchTree(arr)
    bst.in_order(bst.root)
    print(">>>>>>>>>>>>>>>>>")
    node_find = bst.find(70)
    bst.delete_node(70)
    bst.in_order(bst.root)
