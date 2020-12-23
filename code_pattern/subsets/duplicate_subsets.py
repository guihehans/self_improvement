#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: duplicate_subsets.py
@time: 2020/12/23 9:53
@function:

"""


def find_subsets(nums):
    subsets = [[]]
    nums.sort()

    last_generated_subsets = subsets
    for num_idx in range(len(nums)):
        if num_idx > 0 and nums[num_idx] == nums[num_idx - 1]:
            traversed_sets = last_generated_subsets
        else:
            traversed_sets = subsets
        n = len(traversed_sets)
        output_sets = []
        for set_idx in range(n):
            subset = list(traversed_sets[set_idx])
            subset.append(nums[num_idx])
            output_sets.append(subset)
            subsets.append(subset)
        last_generated_subsets = output_sets
    return subsets


def test_null():
    sets = []
    assert find_subsets(sets) == [[]]


def test():
    sets = [1, 3, 3]
    result = [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
    sets_result = list(map(set, result))
    for r in find_subsets(sets):
        assert set(r) in sets_result


def test_1():
    sets = [1, 5, 3, 3]
    result = [[], [1], [5], [3], [1, 5], [1, 3], [5, 3], [1, 5, 3], [3, 3], [1, 3, 3],
              [3, 3, 5],
              [1, 5, 3, 3]]
    sets_result = list(map(set, result))

    for r in find_subsets(sets):
        assert set(r) in sets_result


if __name__ == '__main__':
    test()
