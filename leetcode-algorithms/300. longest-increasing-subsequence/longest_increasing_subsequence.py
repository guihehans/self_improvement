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


class LongestIncreasingSubsequence:
    def __init__(self, nums):
        self.nums = nums

    def dp(self):
        """
        i 为当前扫描指针， j in [0,i-1]
        dp[i]记录当前位置处的最长上升子序列长度
        dp[i]=max(dp[j])+1 for j in [0,i-1] if num[i]>num[j] 否则 跳过
        每一个dp[i] 都要对j 0:i-1扫描
        最终最长的dp为 max(dp)
        :return:
        """
        n = len(self.nums)
        nums = self.nums
        # init dp[i]=1. every subsequence's lis =1
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    continue

        return max(dp)


def test():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    lis = LongestIncreasingSubsequence(nums)
    max_lis = lis.dp()
    print(max_lis)
    assert 4 == max_lis
