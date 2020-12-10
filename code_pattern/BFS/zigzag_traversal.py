#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: zigzag_traversal.py
@time: 2020/12/10 13:48
@function:

"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse_my(root):
    result = []
    queue = deque()
    if root is None:
        return result
    queue.append(root)
    idx = 0
    while queue:
        lvl_size = len(queue)
        cur_lvl = []
        for i in range(lvl_size):
            item = queue.popleft()
            cur_lvl.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        if idx % 2 == 0:
            result.append(cur_lvl)
        elif idx % 2 == 1:
            result.append(cur_lvl[::-1])
        idx += 1
    return result


def traverse(root):
    result = []
    queue = deque()
    if root is None:
        return result
    queue.append(root)
    left_to_right = True
    while queue:
        lvl_size = len(queue)
        cur_lvl = deque()
        for i in range(lvl_size):
            item = queue.popleft()
            if left_to_right:
                cur_lvl.append(item.val)
            else:
                cur_lvl.appendleft(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)

        result.append(list(cur_lvl))
        left_to_right = not left_to_right
    return result


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    assert [[12], [1, 7], [9, 10, 5], [17, 20]] == traverse(root)


def test_null():
    root = None
    assert [] == traverse(root)


if __name__ == '__main__':
    test()
