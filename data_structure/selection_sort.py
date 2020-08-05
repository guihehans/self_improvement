#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: selection_sort.py
@time: 2020/8/5 17:39
@function:

selection sort, each step, select smallest to start, then select smallest in remain and append it to tail.

Time O(n^2)
Space O(1)

"""


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp

    return arr
