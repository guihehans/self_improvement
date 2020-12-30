#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: next_letter_circular.py
@time: 2020/12/30 16:20
@function:

"""
import bisect


def search_next_letter(letters, key):
    n = len(letters)
    start, end = 0, n - 1
    if key > letters[end] or key < letters[0]:
        return letters[0]

    while start <= end:
        mid = start + ((end - start) >> 1)
        mid_value = letters[mid]
        if mid_value < key:
            start = mid + 1
        elif mid_value > key:
            end = mid - 1
        else:  # mid_value==key
            if mid_value == key:
                if mid + 1 < n and letters[mid + 1] > key:
                    return letters[mid + 1]
                elif mid + 1 >= n:
                    return letters[0]
                else:
                    start = mid + 1
    return letters[start]


def test():
    assert (search_next_letter(['a', 'c', 'f', 'h'], 'f')) == 'h'
    assert (search_next_letter(['a', 'c', 'f', 'h'], 'b')) == 'c'
    assert (search_next_letter(['a', 'c', 'f', 'h'], 'm')) == 'a'
    assert (search_next_letter(['a', 'c', 'f', 'h'], 'h')) == 'a'
    assert (search_next_letter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], 'e')) == 'n'
    assert (search_next_letter(["z", "a", "b"], 'z')) == 'z'

    index = bisect.bisect(letters, target)
if __name__ == '__main__':
    test()
