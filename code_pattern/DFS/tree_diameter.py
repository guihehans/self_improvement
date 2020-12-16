#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: tree_diameter.py
@time: 2020/12/16 11:06
@function:

"""
import math

from data_structure.foundamental.read_tree_node import stringToTreeNode, stringToIntegerList


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.get_depth(root)
        return self.treeDiameter

    def get_depth(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)
        # each node will calculate their sub-left,sub-right tree depth.
        # then each node's diameter is left_depth+right_depth.
        # update max_diameter.
        diameter = left_depth + right_depth
        self.treeDiameter = max(self.treeDiameter, diameter)
        # here is best way to get node's depth without passing parameter.
        return max(left_depth, right_depth) + 1


def test():
    tree = "[1, 2, 3, 4, 5]"
    root = stringToTreeNode(tree)
    tree_diameter = TreeDiameter()
    diameter = tree_diameter.find_diameter(root)
    assert diameter == 3


def test_null():
    tree = "[]"
    root = stringToTreeNode(tree)
    tree_diameter = TreeDiameter()
    diameter = tree_diameter.find_diameter(root)
    assert diameter == 0


def test_root():
    tree = "[1, 2, 3]"
    root = stringToTreeNode(tree)
    tree_diameter = TreeDiameter()
    diameter = tree_diameter.find_diameter(root)
    assert diameter == 2


def test_1():
    tree = "[1, 2, 3,null,null,5,6,7,8,9,null,null,null,10,null,11]"
    root = stringToTreeNode(tree)
    tree_diameter = TreeDiameter()
    diameter = tree_diameter.find_diameter(root)
    assert diameter == 6


def test_2():
    tree = "[1, 2]"
    root = stringToTreeNode(tree)
    tree_diameter = TreeDiameter()
    diameter = tree_diameter.find_diameter(root)
    assert diameter == 1


def test_2():
    tree = "[1,2,null,3]"
    root = stringToTreeNode(tree)
    tree_diameter = TreeDiameter()
    diameter = tree_diameter.find_diameter(root)
    assert diameter == 2


if __name__ == '__main__':
    test()
