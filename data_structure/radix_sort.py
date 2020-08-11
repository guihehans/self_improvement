#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: radix_sort.py
@time: 2020/8/11 14:17
@function:

基数排序
针对数字 或者字符串， 可以有高低位的排序。

"""
import math
import unittest


def radix_sort(a, radix=10):
    """
    radix is in which base we can represent number. e.g, 1301913 is a number in 10 radix.

    :param a:
    :param radix: default is 10.
    :return:
    """
    K = int(math.ceil(math.log(max(a) + 1, radix)))  # 用K位数可表示任意整数
    for i in range(1, K + 1):  # K次循环 依照当前位数字排序list
        # 建立1-radix 数据范围的桶，代表1-radix数据范围。 根据当前位的数字
        # 代表在桶的index位置，放入数据，则达到了根据当前位数字排序的目的。 合并桶得到的就是排序后的list
        bucket = [[] for j in range(radix)]
        for val in a:
            # 獲得整數第K位數字 （從低到高）,作为bucket[index], 放入当前数据。
            bucket[val % (radix ** i) // (radix ** (i - 1))].append(val)
        del a[:]
        # 顺次合并桶 得到的就是当前位排序后的list
        for each in bucket:
            a.extend(each)  # 桶合并
    # 各个位均排序后，得到的就是排序好的list
    return a


class TestCase(unittest.TestCase):
    def test(self):
        arr = [1302913, 1402912, 1311311, 1301311]
        target = [1301311, 1302913, 1311311, 1402912]
        self.assertTrue(target == radix_sort(arr))


if __name__ == '__main__':
    unittest.main()
