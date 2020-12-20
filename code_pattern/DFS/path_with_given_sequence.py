#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: path_with_given_sequence.py
@time: 2020/12/11 15:53
@function:

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if root is None or len(sequence) == 0 or sequence[0] != root.val:
        return False
    if root.left is None and root.right is None and len(sequence) == 1:
        return root.val == sequence[0]
    else:
        return find_path(root.left, sequence[1:]) or find_path(root.right, sequence[1:])


def test():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    assert find_path(root, [1, 0, 7]) is False
    assert find_path(root, [1, 1, 6]) is True


def test_true():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    assert find_path(root, [1, 1, 6]) is True


def test_null():
    root = None
    assert find_path(root, [1]) is False


def test_null_seq():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    assert find_path(root, []) is False


if __name__ == '__main__':
    test()
