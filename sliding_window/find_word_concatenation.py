#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_word_concatenation.py
@time: 2020/7/29 14:38
@function:

Given a string and a list of words,
find all the starting indices of substrings in the given string,
that are a concatenation of all the given words exactly once without any overlapping of words.
It is given that all words are of the same length.

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".

"""


def find_word_concatenation(str1, words):
    result_indices = []
    # TODO: Write your code here
    window_start = 0
    slide_start = 0

    matched = 0

    #

    len_word = len(words[0])
    for window_end in range(len(str1)):
        for word in words:
            if word[slide_start] == str1[window_end]:
                slide_start += 1


    return result_indices
