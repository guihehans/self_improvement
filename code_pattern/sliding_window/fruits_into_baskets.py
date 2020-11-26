#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: fruits_into_baskets.py
@time: 2020/7/23 14:23
@function:

Given an array of characters where each character represents a fruit tree,
you are given two baskets and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree.
You will pick one fruit from each tree until you cannot,
i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


It is the same problem with longest substring with k distinct characters.
The problem described in math is equal to:

Find the longest sub string with no more than k=2 characters in a given string.
Return the sub string length.

"""


def fruits_into_baskets(fruits):
    window_start = 0
    window_end = 0
    count_dict = {}
    len_longest = -1
    k = 2
    while window_end < len(fruits):
        count_dict[fruits[window_end]] = count_dict.get(fruits[window_end], 0) + 1
        if len(count_dict) <= k:
            len_longest = max(len_longest, len(fruits[window_start:window_end + 1]))
            window_end = window_end + 1
        else:
            count_dict[fruits[window_start]] = count_dict[fruits[window_start]] - 1
            if count_dict[fruits[window_start]] == 0:
                count_dict.pop(fruits[window_start])
            window_start = window_start + 1

    return len_longest


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
