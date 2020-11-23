#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: longest_increasing_subsequence.py
@time: 2020/11/23 16:10
@function:
给定一个无序的整数数组，找到其中最长上升子序列的长度。
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # init dp[i]=1. every subsequence's lis =1
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    continue

        return max(dp)
