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
    def __init__(self):
        self.cnt = 0

    def find_unique_trees(self, n):
        nums = list(range(1, n + 1))
        for num in nums:
            root = num
            left = [x for x in nums if x < root]
            right = [x for x in nums if x > root]
            self.dfs(left, right)

        return self.cnt

    def dfs(self, left_nums, right_nums):
        if len(left_nums) <= 1 and len(right_nums) <= 1:
            self.cnt += 1
            return

        for node in left_nums:
            lefts = [x for x in right_nums if x < node]
            rights = [x for x in right_nums if x > node]
            self.dfs(lefts, rights)

        for node in right_nums:
            lefts = [x for x in right_nums if x < node]
            rights = [x for x in right_nums if x > node]
            self.dfs(lefts, rights)


def test():
    N = 2
    result = 2
    s = Solution()
    assert s.find_unique_trees(N) == result


def test_1():
    N = 3
    result = 5
    s = Solution()
    assert s.find_unique_trees(N) == result


if __name__ == '__main__':
    test()
