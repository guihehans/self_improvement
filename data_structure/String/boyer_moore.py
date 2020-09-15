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

    def search(self, txt):
        M = self.M
        N = len(txt)
        pat = self.pat
        # bad character rule
        for i in range(0, N - M):
            skip = 0
            for j in range(M - 1, 0, -1):
                if pat[j] != txt[i + j]:
                    # the skip move length is the j-(next occur bad char index in pat).
                    skip = max(1, j - self.bc[ord(txt[i + j])])
                    break
            if skip == 0:
                return i

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
    bm = BoyerMoore(pat)
    print("text:    {}".format(txt))
    offset = bm.search(txt)
    print("pattern:", end=" ")
    for _ in range(0, offset):
        print("", end=" ")
    print(pat)


if __name__ == "__main__":
    main()
