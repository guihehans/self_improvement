#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: pair_with_max_sum.py
@time: 2020/12/17 10:52
@function:

"""

import math

from data_structure.foundamental.read_tree_node import stringToTreeNode

import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_path_sum = -math.inf

    def find_maximum_path_sum(self, root):
        self.get_max_path(root)
        return self.max_path_sum

    def get_max_path(self, root):
        if root is None:
            return 0
        left_path = self.get_max_path(root.left)
        right_path = self.get_max_path(root.right)
        path_over_cur_node = root.val
        if left_path > 0:
            path_over_cur_node += left_path
        if right_path > 0:
            path_over_cur_node += right_path

        self.max_path_sum = max(path_over_cur_node, self.max_path_sum)

        sub_path_sum = max(left_path, right_path)
        if sub_path_sum < 0:
            sub_path_sum = 0
        return sub_path_sum + root.val


def test():
    tree = "[1, 2, 3]"
    solution = Solution()
    root = stringToTreeNode(tree)
    max_path = solution.find_maximum_path_sum(root)
    assert max_path == 6


def test_1():
    tree = "[1, 2, 3,null,4,5,6]"
    solution = Solution()
    root = stringToTreeNode(tree)
    max_path = solution.find_maximum_path_sum(root)
    assert max_path == 16


def test_2():
    tree = "[1,2,3,1,3,5,6,null,null,null,null,7,8,9]"
    solution = Solution()
    root = stringToTreeNode(tree)
    max_path = solution.find_maximum_path_sum(root)
    assert max_path == 31


def test_3():
    tree = "[2,-1]"
    solution = Solution()
    root = stringToTreeNode(tree)
    max_path = solution.find_maximum_path_sum(root)
    assert max_path == 2


def test_4():
    tree = "[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]"
    solution = Solution()
    root = stringToTreeNode(tree)
    max_path = solution.find_maximum_path_sum(root)
    assert max_path == 16


if __name__ == '__main__':
    test()
