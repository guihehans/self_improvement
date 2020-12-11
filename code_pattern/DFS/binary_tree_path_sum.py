#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: binary_tree_path_sum.py
@time: 2020/12/11 10:01
@function:

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == sum

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert has_path(root, 23) is True


def test_1():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert has_path(root, 16) is False


def test_null():
    root = None
    assert has_path(root, 0) is False


def test_negative():
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    assert has_path(root, -5) is True


if __name__ == '__main__':
    test()
