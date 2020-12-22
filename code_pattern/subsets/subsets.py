#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: subsets.py
@time: 2020/12/22 13:58
@function:

"""


def find_subsets_0(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            # add list() to ensure construct new copy, not operate on subsets element.
            sub_set = list(subsets[i])
            sub_set.append(num)
            # add new subset back
            subsets.append(sub_set)

    return subsets


def find_subsets(nums):
    result = []
    n = len(nums)
    # n=3,num取值 000-111 也可以叫mask
    for mask in range(1 << n):
        t = []
        # 挨个检查mask每一位 如果某位是1 此元素加入。
        for i in range(n):
            if mask & 1 << i:
                t.append(nums[i])
        result.append(t)
    return result


def test_null():
    sets = []
    assert find_subsets(sets) == [[]]


def test():
    sets = [1, 3]
    assert find_subsets(sets) == [[], [1], [3], [1, 3]]


def test_1():
    sets = [1, 5, 3]
    assert find_subsets(sets) == [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]


if __name__ == '__main__':
    test()
