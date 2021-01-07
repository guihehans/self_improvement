#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: sort_string_by_frequency.py
@time: 2021/1/7 16:19
@function:

"""

from heapq import *


def sort_character_by_frequency(s):
    freq_map = {}
    for c in s:
        freq_map[c] = freq_map.get(c, 0) + 1

    max_heap = []
    for char, freq in freq_map.items():
        heappush(max_heap, (-freq, char))

    result = ""
    while max_heap:
        freq, char = heappop(max_heap)
        result += char * -freq

    return result


def test():
    src_str = "Programming"
    expected = "ggmmrrPaino"
    assert sort_character_by_frequency(src_str) == expected


def test_2():
    src_str = "abcbab"
    expected = "bbbaac"
    assert sort_character_by_frequency(src_str) == expected


def test_3():
    src_str = "Aabb"
    expected = "bbAa"
    assert sort_character_by_frequency(src_str) == expected


if __name__ == '__main__':
    test()
