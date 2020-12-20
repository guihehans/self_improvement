#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: sum_root_to_leaf_numbers.py
@time: 2020/12/11 15:00
@function:

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers_my(root):
    all_sum = []
    sums = 0
    dfs(root, sums, all_sum)
    return sum(all_sum)


def dfs(root, path_sum, all_sum):
    if root is None:
        return
    current_sum = path_sum * 10 + root.val
    if root.left is None and root.right is None:
        all_sum.append(current_sum)
    else:
        dfs(root.left, current_sum, all_sum)
        dfs(root.right, current_sum, all_sum)


def find_sum_of_path_numbers(root):
    return dfs_(root, 0)


def dfs_(root, path_sum):
    if root is None:
        return 0

    current_sum = path_sum * 10 + root.val
    if root.left is None and root.right is None:
        return current_sum
    else:
        return dfs_(root.left, current_sum) + dfs_(root.right, current_sum)


def test():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    assert find_sum_of_path_numbers(root) == 332


def test_1():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    assert find_sum_of_path_numbers(root) == 408


def test_null():
    root = None
    assert find_sum_of_path_numbers(root) == 0


def test_negative():
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    assert find_sum_of_path_numbers(root) == -23


if __name__ == '__main__':
    test()
