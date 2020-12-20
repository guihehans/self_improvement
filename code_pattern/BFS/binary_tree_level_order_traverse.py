#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: binary_tree_level_order_traverse.py
@time: 2020/12/9 17:54
@function:

"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
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

        result.append(current_level)

    return result


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert [[12], [7, 1], [9, 10, 5]]== traverse(root)


def test_null():
    root = None
    assert [] == traverse(root)


if __name__ == '__main__':
    test()
