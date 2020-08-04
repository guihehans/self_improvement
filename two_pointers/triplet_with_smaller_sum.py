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


"""
Similar Problems #
Problem: Write a function to return the list of all such triplets instead of the count.
How will the time complexity change in this case?
"""

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        search_pair(arr, target - arr[i], i, triplets)
    return triplets


def search_pair(arr, target_sum, first, triplets):
    """
    similar idea.
    Time. O(N^3, since there is inner loop for adding triplets)
    Space. O(N)

    :param arr:
    :param target_sum:
    :param first:
    :param triplets:
    :return:
    """
    left = first + 1
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum:  # found the triplet
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
            for i in range(right, left, -1):
                triplets.append([arr[first], arr[left], arr[i]])
            left += 1
        else:
            right -= 1  # we need a pair with a smaller sum


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
