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
    """
    define a word_frequency map for recording word.
    define a word seen map for word if seen or not.

    use a double loop, first loop to iterate the words total concatenation long,
    second loop to iterate word long, to compare the word long str if equal to word in words.

    if word seen, break
    if word not in words, break,
    if all concatenation long str can match the words, return the index, append it to result list.

    assume N= len of str. M= count of word. len= length of word.
    Time complexity O(N*M*len)
    Space complexity O(M+N) M for two hashmap. N for result list.
    :param str1:
    :param words:
    :return:
    """
    if len(words) == 0 or len(words[0]) == 0:
        return []

    # init word freq map
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    # init len word
    len_word = len(words[0])
    count_word = len(words)

    result_indices = []

    for i in range(len(str1) - len_word * count_word + 1):
        # in each iteration, init word_seen to record seen word or not
        word_seen = {}
        for j in range(count_word):
            next_word_index = i + j * len_word
            # Get the next word from the string
            word = str1[next_word_index: next_word_index + len_word]
            if word not in word_freq:
                break

            if word not in word_seen:
                word_seen[word] = 0
            word_seen[word] += 1

            # if word has been seen more than it should be in frequency, break
            if word_seen[word] > word_freq.get(word, 0):
                break

            if j == count_word - 1:
                result_indices.append(i)

    return result_indices


def main_test():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))
    print(find_word_concatenation("cacatcatfoxfox", ["cat", "fox"]))


if __name__ == '__main__':
    main_test()
