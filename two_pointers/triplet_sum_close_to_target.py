#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: triplet_sum_close_to_target.py
@time: 2020/8/3 15:10
@function:
Given an array of unsorted numbers and a target number,
find a triplet in the array whose sum is as close to the target number as possible,
return the sum of the triplet. If there are more than one such triplet,
return the sum of the triplet with the smallest sum.

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

"""


def search_pair(arr, i, target_sum, tmp_sum):
    pass

def find_closest_sum(closest_sum, target_sum):
    pass


def triplet_sum_close_to_target(arr, target_sum):
    closest_sum = 0
    arr.sort()
    min_diff = 25555

    for i in range(len(arr) - 2):
        cur_num = arr[i]
        left = arr[i + 1]
        right = arr[len(arr) - 1]
        cur_sum = cur_num + left + right
        diff = abs(target_sum - cur_num)

        while left < right:
            if diff == 0:
                return cur_num
            else:
                min_diff = min(min_diff, diff)
                closest_sum = cur_num

                if cur_sum < target_sum:
                    left += 1
                elif cur_sum > target_sum:
                    right -= 1

        return closest_sum
