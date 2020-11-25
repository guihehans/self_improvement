"""
@author: guihehans
@file: shortest_window_sort.py 
@time: 2020/11/25 21:37
@function:
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
Example 1:
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:
Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Example 3:
Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted
Example 4:
Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""

import math


def shortest_window_sort(nums):
    low, high = 0, len(nums) - 1
    while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
        low += 1
    # if low reach end, all sorted, return 0
    if low == len(nums) - 1:
        return 0
    while high > 0 and nums[high] >= nums[high - 1]:
        high -= 1

    # get the max,min in [low,high]
    max_val = -math.inf
    min_val = math.inf
    for k in range(low, high + 1):
        max_val = max(max_val, nums[k])
        min_val = min(min_val, nums[k])

    # extend low for [0,low) >min arr[low] already be must > min, since low+1 is invert point
    while low > 0 and nums[low - 1] > min_val:
        low -= 1
    # extend high for (high,n-1] <max
    while high < len(nums) - 1 and nums[high + 1] < max_val:
        high += 1

    return high - low + 1


def test_0():
    arr = [1, 2, 5, 3, 7, 10, 9, 12]
    assert 5 == shortest_window_sort(arr)


def test_1():
    arr = [1, 3, 2, 0, -1, 7, 10]
    assert 5 == shortest_window_sort(arr)


def test_2():
    arr = [1, 2, 3]
    assert 0 == shortest_window_sort(arr)


def test_3():
    arr = [3, 2, 1]
    assert 3 == shortest_window_sort(arr)


if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    test_3()
