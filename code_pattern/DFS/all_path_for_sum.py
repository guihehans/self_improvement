#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: all_path_for_sum.py
@time: 2020/12/11 11:28
@function:

"""
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    path_stack = deque()
    dfs(root, sum, path_stack, allPaths)

    return allPaths


def dfs(root, sum, path, allPaths):
    if root is None:
        return

    path.append(root.val)

    if root.left is None and root.right is None and root.val == sum:
        allPaths.append(list(path))
    else:
        dfs(root.left, sum - root.val, path, allPaths)
        dfs(root.right, sum - root.val, path, allPaths)

    del path[-1]


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    assert find_paths(root, sum) == [[12, 7, 4], [12, 1, 10]]


def test_1():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)
    sum = 12
    assert find_paths(root, sum) == [[1, 7, 4], [1, 9, 2]]


def test_null():
    root = None
    sum = 0
    assert find_paths(root, sum) == []


def test_negative():
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    sum = -5
    assert find_paths(root, sum) == [[-2, -3]]


if __name__ == '__main__':
    test()
