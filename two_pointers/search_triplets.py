#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: search_triplets.py
@time: 2020/7/31 14:45
@function:

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

"""


def search_for_pair(arr, i):
    pair = []
    cur = arr[i]
    to_find_sum = - cur
    left = i + 1
    right = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] < to_find_sum or arr[left] == arr[i]:
            left += 1
        elif arr[left] + arr[right] > to_find_sum:
            right -= 1
        else:
            if arr[left] != arr[right]:
                return [arr[i], arr[left], arr[right]]
            else:
                return []


def search_triplets(arr):
    result_list = []
    arr.sort()

    for i in range(len(arr)):
        pair = search_for_pair(arr, i)
        if pair:
            result_list.append(pair)

    return result_list


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
