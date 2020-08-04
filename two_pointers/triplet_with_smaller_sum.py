#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: triplet_with_smaller_sum.py
@time: 2020/8/4 10:37
@function:

Given an array arr of unsorted numbers and a target sum,
count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.

Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Input: [-1, 4, 2, 1, 3], target=5
Output: 4
Explanation: There are four triplets whose sum is less than the target:
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

"""


def triplet_with_smaller_sum(arr, target):
    """
    similar to triple sum.
    with loop through SORTED array, the head and and tail can be set.
    when sum is less than target, then all right -- can be counted.
    then move left ++ for another round scan.

    when sum is larger than target, then right --, to check if other fits.

    Time. Sort O(N* logN). double loop O(N^2) total O(N*logN +N^2)= O(N^2)
    Space. O(N) for sort if sort is not in space.
    :param arr:
    :param target:
    :return:
    """
    count = 0
    arr.sort()

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            cur_sum = arr[i] + arr[left] + arr[right]
            # improved, can get the count by right-left
            if cur_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1

    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
