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


def triplet_sum_close_to_target(arr, target_sum):
    """
    again, sort the array first. O(N*logN)
    loop the array as 1st element of triplet. second as head and tail as end.
    compare the current sum with target sum. according if the diff is the smaller to change
    the to return closest sum. if the diff is same , closest sum is smaller one.
    if sum < taget sum ,the head++
    if sum > target sum, the end--
    return the global found closest sum.

    :param arr:
    :param target_sum:
    :return:
    """
    closest_sum = 0
    arr.sort()
    min_diff = 25555

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            cur_sum = arr[i] + arr[left] + arr[right]
            diff = abs(target_sum - cur_sum)
            if diff == 0:
                return cur_sum
            else:
                if diff == min_diff:
                    closest_sum = min(cur_sum, closest_sum)
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = cur_sum

                if cur_sum < target_sum:
                    left += 1
                elif cur_sum > target_sum:
                    right -= 1

    return closest_sum


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
