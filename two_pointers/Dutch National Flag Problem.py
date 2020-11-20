#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: Dutch National Flag Problem.py
@time: 2020/8/5 15:49
@function:

Given an array containing 0s, 1s and 2s, sort the array in-place.
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue;
and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]

"""
from data_structure.PQ.MaxPQ import MaxHeap


def dutch_flag_sort(arr):
    """
    bf version, the key is treat numbers as objects
    use MaxHeap to heap sort the arr.
    Time: O(n*logn)
    Space O(N)
    :param arr:
    :return:
    """
    heap = MaxHeap(arr)
    heap.sort()
    return heap.array


def dutch_flag_sort_two_pointer(arr):
    """
    since only 3 kinds of data, move all 0 before low,
    and move all 2 after high. then only 1s are between 0 and 2.
    so only 3 condition
    1 arr[i]==0: swap arr[i],arr[low]. i++ low++
    2 arr[i]==1: i++
    3 arr[i]==2: swap arr[i], arr[high]. high--
    the swapped element,even equal values, can restore sequence in next run.
    Time O(N)
    Space in place.O(1)
    :param arr:
    :return:
    """
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 1:
            i += 1
        elif arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
    return arr


def main():
    f = dutch_flag_sort_two_pointer
    arr = [1, 0, 2, 1, 0]
    print(f(arr))
    arr2 = [2, 2, 0, 1, 2, 0]
    print(f(arr2))


if __name__ == '__main__':
    main()
