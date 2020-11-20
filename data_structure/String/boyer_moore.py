#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: boyer_moore.py
@time: 2020/9/11 16:54
@function:

"""
import sys


class BoyerMoore:
    def __init__(self, pattern):
        self.pat = pattern
        self.M = len(pattern)
        # ascii size
        self.R = 256
        # a hashtable with R size, called bad characters bc
        self.bc = [-1 for i in range(0, self.R)]
        # store the latest index for characters in pattern, in corresponding index of ascii value in bc
        for j in range(self.M):
            self.bc[ord(pattern[j])] = j
        # good suffix rule data structure init
        self.suffix = [-1 for i in range(self.M)]
        self.prefix = [False for i in range(self.M)]
        self.generate_good_suffix(pattern, self.suffix, self.prefix)

    def generate_good_suffix(self, pattern: str, suffix, prefix):
        """
        init the suffix and prefix array.

        :param pattern: the given pattern str
        :param suffix:  the suffix array, index is the length of pattern's
        suffix(range from [1:m]), the value is matched sub string in pattern's index.
        :param prefix: the prefix array, index is the length of pattern's suffix,
                    the value is if this suffix is a matched prefix(index from 0).
        :return:
        """
        M = self.M
        # i is the index of scanning index in pattern, range from [0,M-2], to scan substring before pattern[M-1]
        for i in range(M - 1):
            # j is the index of suffix index
            j = i
            # k is the suffix array length, also index, should range from [1,M-1]
            k = 0
            while j >= 0 and pattern[j] == pattern[M - 1 - k]:
                j -= 1
                k += 1
                suffix[k] = j + 1
            if j == -1:
                prefix[k] = True

    def move_by_good_suffix(self, j, m, suffix, prefix) -> int:
        """
        the moving algorithm for good suffix rule when bad character at j happens.
        current good suffix's len is k.

        1. check if there's a match in suffix[k]. which means x= suffix[k]!=-1
            if found, move index is j-x+1
        2. if no match(x==-1),scan the suffix collections of good suffix pattern[r,m-1],
            length k =m-r, r range from[j+2,m-1], find the longest prefix can match suffix.
            if prefix[k] is True, move index =r-0=r


        :param j: the bad character occur's index
        :param m: the length of pattern
        :param suffix: the preprocessed suffix array
        :param prefix: the preprocessed prefix array
        :return: the move index
        """
        # k is the good suffix length
        k = m - 1 - j
        if suffix[k] != -1:
            return j - suffix[k] + 1
        # r is the sub suffix index, range from [j+2,m-1]
        for r in range(j + 2, m):
            sub_len = m - r
            if prefix[sub_len]:
                return r
        # if none found, move the entire pattern.
        return m

    def search(self, txt):                                                                                                                     


        M = self.M
        N = len(txt)
        pat = self.pat
        # bad character rule
        skip = 0
        i = 0
        while i <= N - M:
            skip = 0
            for j in range(M - 1, -1, -1):
                if pat[j] != txt[i + j]:
                    # the skip move length is the j-(next occur bad char index in pat).
                    skip = j - self.bc[ord(txt[i + j])]
                    if skip < 1:
                        skip = 1
                    break
            if skip == 0:
                return i
            i += skip
        return N

    def search_with_good_suffix_rule(self, txt):
        M = self.M
        N = len(txt)
        pat = self.pat
        # i is the cursor in txt string
        i = 0
        while i <= N - M:
            # scan pattern backwards,range from [M-1,0]
            for j in range(M - 1, -1, -1):
                if txt[i + j] != pat[j]:
                    break
            # now j is the index of bad character
            if j == 0:  # j == 0, matched.
                return i
            # x is the bad character rule move index
            x = j - self.bc[ord(txt[i + j])]
            # y set to 0 in case x<0
            y = 0
            # if j<M-1, there's good suffix, apply good suffix rule
            if j < M - 1:
                y = self.move_by_good_suffix(j, M, self.suffix, self.prefix)
            i = i + max(x, y)

        return -1


def main():
    """Takes a pattern string and an input string as command-line arguments;
    searches for the pattern string in the text string; and prints the first
    occurrence of the pattern string in the text string.
    Will print the pattern after the end of the string if no match is
    found.
    """
    pat = sys.argv[1]
    txt = sys.argv[2]
    bm = BoyerMoore(pat)
    print("text:    {}".format(txt))
    offset = bm.search(txt)
    print("pattern:", end=" ")
    for _ in range(0, offset):
        print("", end=" ")
    print(pat)

    print("text:    {}".format(txt))
    offset = bm.search_with_good_suffix_rule(txt)
    print("pattern:", end=" ")
    for _ in range(0, offset):
        print("", end=" ")
    print(pat)


if __name__ == "__main__":
    main()
