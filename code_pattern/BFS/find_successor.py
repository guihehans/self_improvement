#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_successor.py
@time: 2020/12/10 15:49
@function:

"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    last_node = None
    while queue:
        item = queue.popleft()
        if last_node and last_node.val == key:
            return item
        if item.left:
            queue.append(item.left)
        if item.right:
            queue.append(item.right)
        last_node = item


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


if __name__ == '__main__':
    test()
