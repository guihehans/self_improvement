#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: connect_level_order_siblings.py
@time: 2020/12/10 16:11
@function:

"""

from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings_my(root):
    if root is None:
        return root
    queue = deque()
    queue.append(root)

    while queue:
        lvl_size = len(queue)
        last_node = None
        for i in range(lvl_size):
            cur_node = queue.popleft()
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
            if last_node:
                last_node.next = cur_node
            last_node = cur_node

    return root


def connect_level_order_siblings(root):
    if root is None:
        return root
    queue = deque()
    queue.append(root)

    while queue:
        lvl_size = len(queue)
        for i in range(lvl_size):
            cur_node = queue.popleft()
            # 只有i<lvl_size-1,即非层末元素,才需要链接
            if i < lvl_size - 1:
                cur_node.next = queue[0]
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    return root


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


if __name__ == '__main__':
    test()
