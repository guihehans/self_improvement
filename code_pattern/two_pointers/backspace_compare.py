#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: backspace_compare.py
@time: 2020/11/25 15:24
@function:
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
"""


def backspace_compare_1(str1, str2):
    """
    compare in reverse order, so we can know whether if a char to delete or not.
    using a skip_1,skip_2 to record if a char need to be delete.

    :param str1:
    :param str2:
    :return:
    """
    i, j = len(str1) - 1, len(str2) - 1
    skip_1, skip_2 = 0, 0
    # until i j ALL <0, the scan is over. so use OR
    while i >= 0 or j >= 0:
        # process '#' repeatedly until str[i]!=# and skip==0,unless i<0
        while i >= 0:
            if str1[i] == "#":
                skip_1 += 1
                i -= 1
            elif skip_1 != 0:
                skip_1 -= 1
                i -= 1
            else:
                break
        while j >= 0:
            if str2[j] == "#":
                skip_2 += 1
                j -= 1
            elif skip_2 != 0:
                skip_2 -= 1
                j -= 1
            else:
                break

        if i >= 0 and j >= 0:
            if str1[i] != str2[j]:
                return False
        elif i >= 0 or j >= 0:
            return False
        # match, i-- j--
        i -= 1
        j -= 1
    if i != j:
        return False
    return True


def backspace_compare(str1, str2):
    # use two pointer approach to compare the strings
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_char_index(str1, index1)
        i2 = get_next_valid_char_index(str2, index2)
        if i1 < 0 and i2 < 0:  # reached the end of both the strings
            return True
        if i1 < 0 or i2 < 0:  # reached the end of one of the strings
            return False
        if str1[i1] != str2[i2]:  # check if the characters are equal
            return False

        index1 = i1 - 1
        index2 = i2 - 1

    return True


def get_next_valid_char_index(str, index):
    backspace_count = 0
    while index >= 0:
        if str[index] == '#':  # found a backspace character
            backspace_count += 1
        elif backspace_count > 0:  # a non-backspace character
            backspace_count -= 1
        else:
            break

        index -= 1  # skip a backspace or a valid character

    return index


def test_0():
    s1 = "bxj##tw"
    s2 = "bxj###tw"
    assert backspace_compare(s1, s2) is False


def test_1():
    s1 = "a##c"
    s2 = "#a#c"
    assert backspace_compare(s1, s2) is True


def test_2():
    s1 = "xywrrmp"
    s2 = "xywrrmu#p"
    assert backspace_compare(s1, s2) is True


def test_3():
    s1 = "xp#"
    s2 = "xyz##"
    assert backspace_compare(s1, s2) is True


def test_4():
    s1 = "nzp#o#g"
    s2 = "b#nzp#o#g"
    assert backspace_compare(s1, s2) is True


if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    test_3()
    test_4()
