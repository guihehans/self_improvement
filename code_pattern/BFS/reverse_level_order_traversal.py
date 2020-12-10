#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: reverse_level_order_traversal.py
@time: 2020/12/10 11:26
@function:

"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root: TreeNode):
    result = []
    if root is None:
        return []

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        cur_level = []
        for _ in range(level_size):
            item = queue.popleft()
            cur_level.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        result.append(cur_level)
    return result[::-1]


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert [[9, 10, 5], [7, 1], [12]] == traverse(root)


def test_null():
    root = None
    assert [] == traverse(root)


if __name__ == '__main__':
    test()
