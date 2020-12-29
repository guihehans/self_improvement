#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_unique_trees_to_store_n.py
@time: 2020/12/28 16:18
@function:

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def find_unique_trees(self, n):
        if n <= 0:
            return []
        return find_unique_trees_recursively(1, n)


def find_unique_trees_recursively(start, end):
    result = []
    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left_subtrees = find_unique_trees_recursively(start, i - 1)
        right_subtrees = find_unique_trees_recursively(i + 1, end)
        for left_tree in left_subtrees:
            for right_tree in right_subtrees:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                result.append(root)

    return result


def test():
    N = 2
    result = 2
    s = Solution()
    assert len(s.find_unique_trees(N)) == result


def test_1():
    N = 3
    result = 5
    s = Solution()
    assert len(s.find_unique_trees(N)) == result


def test_3():
    N = 4
    result = 14
    s = Solution()
    assert len(s.find_unique_trees(N)) == result


def test_4():
    N = 5
    result = 42
    s = Solution()
    assert len(s.find_unique_trees(N)) == result


if __name__ == '__main__':
    test()
