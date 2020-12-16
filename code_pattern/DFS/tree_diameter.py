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
        if root is None:
            return 0
        self.treeDiameter = max(self.treeDiameter, get_diameter(root, 0))
        self.treeDiameter = max(self.treeDiameter, self.find_diameter(root.left))
        self.treeDiameter = max(self.treeDiameter, self.find_diameter(root.right))
        return self.treeDiameter


def get_diameter(root, level):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    left_path = get_max_path(root.left, level + 1)
    right_path = get_max_path(root.right, level + 1)
    return left_path + right_path


def get_max_path(node: TreeNode, level: int) -> int:
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return level
    left_depth = get_max_path(node.left, level + 1)
    right_depth = get_max_path(node.right, level + 1)
    return max(left_depth, right_depth)


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
