#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: count_paths_for_sum.py
@time: 2020/12/11 17:29
@function:

"""
from data_structure.foundamental.read_tree_node import stringToTreeNode, stringToIntegerList


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return dfs(root, S)


def find_path(path, sum_val):
    pass


def dfs(root, sum_val):
    if root is None:
        return 0
    if root.val == sum_val:
        return 1
    else:
        return dfs(root.left, sum_val) \
               + dfs(root.right, sum_val) \
               + dfs(root.left, sum_val - root.val) \
               + dfs(root.right, sum_val - root.val)


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert count_paths(root, 11) == 2


def test_1():
    tree = "[10,5,-3,3,2,null,11,3,-2,null,1]"
    test_data = "8"
    root = stringToTreeNode(tree)
    arr = stringToIntegerList(test_data)
    assert count_paths(root, arr) == 3


def test_null():
    root = None
    assert count_paths(root, 1) == 0


if __name__ == '__main__':
    test()
