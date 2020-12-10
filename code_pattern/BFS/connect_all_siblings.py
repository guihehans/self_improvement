#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: connect_all_siblings.py
@time: 2020/12/10 16:57
@function:

"""
from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if root is None:
        return root
    queue = deque()
    queue.append(root)

    while queue:

        cur_node = queue.popleft()

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
        if len(queue) > 0:
            cur_node.next = queue[0]

    return root


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


if __name__ == '__main__':
    test()
