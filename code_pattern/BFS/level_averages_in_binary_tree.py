#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: level_averages_in_binary_tree.py
@time: 2020/12/10 14:51
@function:

"""
import math
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        level_size = len(queue)
        avg = 0
        for _ in range(level_size):
            item = queue.popleft()
            avg += item.val
            if item.left is not None:
                queue.append(item.left)
            if item.right is not None:
                queue.append(item.right)
        if level_size != 0:
            result.append(avg / level_size)
        else:
            result.append(0)

    return result


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert [12.0, 4.0, 6.5] == find_level_averages(root)


def test_null():
    root = None
    assert [] == find_level_averages(root)


def test_0():
    root = TreeNode(0)
    assert [0] == find_level_averages(root)


if __name__ == '__main__':
    test()
