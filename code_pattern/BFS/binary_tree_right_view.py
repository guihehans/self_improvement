#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: binary_tree_right_view.py
@time: 2020/12/10 17:05
@function:

"""
from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            item = queue.popleft()
            current_level.append(item.val)
            if item.left is not None:
                queue.append(item.left)
            if item.right is not None:
                queue.append(item.right)

        result.append(current_level[-1])

    return result


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    assert [12, 1, 5, 3] == result


if __name__ == '__main__':
    test()
