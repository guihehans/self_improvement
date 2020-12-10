#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: minimum_depth_of_binary_tree.py
@time: 2020/12/10 15:20
@function:

"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    cur_level = 1
    while queue:
        lvl_size = len(queue)
        for _ in range(lvl_size):
            item = queue.popleft()
            if item.left is None and item.right is None:
                return cur_level
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)

        cur_level += 1
    return -1


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


if __name__ == '__main__':
    test()
