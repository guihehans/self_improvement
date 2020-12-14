#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: count_paths_for_sum.py
@time: 2020/12/11 17:29
@function:

"""
from data_structure.foundamental.read_tree_node import stringToTreeNode, stringToIntegerList


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return dfs(root, S, [])


def dfs(root, sum_val, current_path):
    if root is None:
        return 0
    # add current node to path
    current_path.append(root.val)

    # find all subset path sum of current path
    path_count, path_sum = 0, 0
    for i in range(len(current_path)-1, -1, -1):
        path_sum += current_path[i]
        if path_sum == sum_val:
            path_count += 1
    # traverse left subtree and right subtree
    path_count += dfs(root.left, sum_val, current_path)
    path_count += dfs(root.right, sum_val, current_path)

    # remove current node for backtrack
    del current_path[-1]
    return path_count


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert count_paths(root, 11) == 2


def test_1():
    tree = "[10,5,-3,3,2,null,11,3,-2,null,1]"
    test_data = "8"
    root = stringToTreeNode(tree)
    arr = stringToIntegerList(test_data)
    assert count_paths(root, arr) == 3


def test_2():
    tree = "[1,-2,-3,1,3,-2,null,-1]"
    test_data = "3"
    root = stringToTreeNode(tree)
    arr = stringToIntegerList(test_data)
    assert count_paths(root, arr) == 1


def test_null():
    root = None
    assert count_paths(root, 1) == 0


if __name__ == '__main__':
    test()
