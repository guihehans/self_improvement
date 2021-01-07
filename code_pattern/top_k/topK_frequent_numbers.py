#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: topK_frequent_numbers.py
@time: 2021/1/7 15:16
@function:

"""

from heapq import *


def find_k_frequent_numbers(nums, k):
    topNumbers = []
    freq_map = {}
    n = len(nums)
    for i in range(n):
        freq_map = add_freq(freq_map, nums[i])

    i = 0
    for num, freq in freq_map.items():
        if i < k:
            heappush(topNumbers, (freq, num))
        else:
            if freq > topNumbers[0][0]:
                heappushpop(topNumbers, (freq, num))
        i += 1

    result = []
    for j in range(k):
        result.append(topNumbers[j][1])
    return result


def add_freq(freq, item):
    if item not in freq:
        freq[item] = 1
    else:
        freq[item] += 1

    return freq


def test():
    arr = [1, 3, 5, 12, 11, 12, 11]
    k = 2
    expected = [12, 11]
    assert set(find_k_frequent_numbers(arr, k)) == set(expected)


def test_2():
    arr = [1]
    k = 1
    expected = [1]
    assert set(find_k_frequent_numbers(arr, k)) == set(expected)


def test_3():
    arr = [1, 1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2]
    assert set(find_k_frequent_numbers(arr, k)) == set(expected)


if __name__ == '__main__':
    test()
