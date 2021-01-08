#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: rearrange_string.py
@time: 2021/1/8 17:13
@function:

"""
from collections import deque
from heapq import *


def rearrange_string(S):
    freq_map = {}
    for char in S:
        freq_map[char] = freq_map.get(char, 0) + 1

    max_heap = []
    for char, freq in freq_map.items():
        heappush(max_heap, (-freq, char))

    n = len(S)
    result = ""
    while max_heap:
        for i in range(len(max_heap)):
            freq, char = max_heap[i]
            if result and result[-1] == char:
                return ""
            result = result + char
            freq += 1
            if freq == 0:
                del max_heap[i]
                break
            else:
                max_heap[i] = (freq, char)

    return result


def no_char_repeat(S):
    n = len(S)
    if n >= 1:
        for i in range(n - 1):
            if S[i] == S[i + 1]:
                return False
        return True
    else:
        return True


def test():
    input = "aappp"
    result = rearrange_string(input)
    assert no_char_repeat(result) is True


def test_1():
    input = "programming"
    result = rearrange_string(input)
    assert no_char_repeat(result) is True


def test_2():
    input = "aapa"
    result = rearrange_string(input)
    assert no_char_repeat(result) is True


def test_3():
    input = "aab"
    result = rearrange_string(input)
    assert no_char_repeat(result) is True


def test_4():
    input = "vvvlo"
    result = rearrange_string(input)
    assert no_char_repeat(result) is True

def test_4():
    input = "kkkkzrkatkwpkkkktrq"
    result = rearrange_string(input)
    assert no_char_repeat(result) is True


if __name__ == '__main__':
    test()
