#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: kmp.py
@time: 2020/9/18 9:51
@function:

THe KMP algorithm, compare from left to right.
Time : O(N+M)
space: O(M)
"""
from typing import List


class KMP:

    def __init__(self, pattern):
        self.pattern = pattern
        self.M = len(pattern)
        self.next = self.generate_next(pattern, self.M)

    def generate_next(self, pattern, M) -> List[int]:
        """
        the next array(also called failure function),store the prefix's longest match sub prefix info.

        the index is the prefix's ending char index,range from [0,M-1],

        the value is the longest suffix match sub prefix's ending char index.-1 if not exist.

        ## idea:
        for k=-1 version, the k is the longest pre match suffix's last index.
        one suffix's index will contain its sub's sub optimal longest match's index.
        so k=next[k]. loop until no match found(k=-1)
        then check if pattern's next char == current end char, if found ,k++.
        now next[i]=k
        Time complexity =O(M)

        another version is k=0 version which k is longest pre match suffix char number.

        :param pattern: the pattern string
        :param M: length of pattern
        :return:next_arr
        """
        next_arr = [-1 for _ in range(M)]
        next_arr[0] = -1
        k = -1
        for i in range(1, M):
            while k != -1 and pattern[k + 1] != pattern[i]:
                k = next_arr[k]
            if pattern[k + 1] == pattern[i]:
                k += 1
            next_arr[i] = k

        return next_arr

    def search(self, txt):
        """
        when match failed, txt index dont change, patten index m change back by next[j-1]+1.
        then check updated txt[i] == pattern[j], if match, j++.
        if j reach end, all match and return i-M+1.

        :param txt:
        :return:
        """
        N = len(txt)
        M = self.M
        pattern = self.pattern
        next = self.next
        j = 0
        for i in range(N):
            while j > 0 and txt[i] != pattern[j]:
                j = next[j - 1] + 1
            if txt[i] == pattern[j]:
                j += 1
            if j == M:
                return i - M + 1

        return N


def main():
    """Takes a pattern string and an input string as command-line arguments;
    searches for the pattern string in the text string; and prints the first
    occurrence of the pattern string in the text string.
    Will print the pattern after the end of the string if no match is
    found.
    """
    pat = sys.argv[1]
    txt = sys.argv[2]
    kmp = KMP(pat)
    print("text:    {}".format(txt))
    offset = kmp.search(txt)
    print("pattern: ", end="")
    for _ in range(0, offset):
        print("", end=" ")
    print(pat)


if __name__ == "__main__":
    import sys

    main()
