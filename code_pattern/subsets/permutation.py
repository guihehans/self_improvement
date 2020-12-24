#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: permutation.py
@time: 2020/12/23 11:27
@function:

"""


class Permutation:
    def find_permutations(self, nums):
        result = []

        def search(cur_nums, permutation):
            """
            :param cur_nums: the passed current available nums list.
            :param permutation: the passed current permutation list.
            :return:
            """
            # if passed cur_nums is [],append permutation
            if not cur_nums:
                result.append(permutation)
                return
            for i in range(len(cur_nums)):
                # make a new list excluding nums[i].
                excluded_list = cur_nums[:i] + cur_nums[i + 1:]
                # make a new list copying passing permutation.
                tmp = list(permutation)
                tmp.append(cur_nums[i])
                search(excluded_list, tmp)

        search(nums, [])
        return result


def test():
    arr = [1, 3, 5]
    solution = Permutation()
    result = solution.find_permutations(arr)
    expected = [[1, 3, 5], [1, 5, 3], [3, 1, 5], [3, 5, 1], [5, 1, 3], [5, 3, 1]]
    for r in result:
        assert r in expected
