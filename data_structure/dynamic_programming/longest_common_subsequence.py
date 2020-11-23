#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: longest_common_subsequence.py
@time: 2020/11/23 15:35
@function:
given two string a,b with length n,m;
get the longest common subsequence number.

e.g.,
"mitcmu"
"mtacnu"

lsc=4 mtcu

"""


class LongestCommonSequence:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def max_lcs(self):
        """
        dp to get longest common subsequence
        max_lcs(i,j) means the lcs of a[0:i] and b[0:j]
        the states formula is:
        max_lcs(i,j)=  max(max_lcs(i-1,j-1)+1,max_lcs(i-1,j),max_lcs(i,j-1))      if a[i]==b[j]
                    =  max(max_lcs(i-1,j-1),max_lcs(i-1,j),max_lcs(i,j-1))            a[i]!=b[j]

        :return:
        """
        a, b = self.a, self.b
        n, m = len(self.a), len(self.b)
        states = [[0 for j in range(m)] for i in range(n)]
        # init row 0
        for j in range(m):
            if a[0] == b[j]:
                states[0][j] = 1
            elif j == 0:
                states[0][j] = 0
            else:
                states[0][j] = states[0][j - 1]
        # init col 0
        for i in range(n):
            if b[0] == a[i]:
                states[i][0] = 1
            elif i == 0:
                states[i][0] = 0
            else:
                states[i][0] = states[i - 1][0]

        # fill the rest
        for i in range(1, n):
            for j in range(1, m):
                if a[i] == b[j]:
                    states[i][j] = max(states[i - 1][j - 1] + 1, states[i - 1][j], states[i][j - 1])
                else:
                    states[i][j] = max(states[i - 1][j - 1], states[i - 1][j], states[i][j - 1])

        return states[n - 1][m - 1]


def test():
    a = "mitcmu"
    b = "mtacnu"
    lcs = LongestCommonSequence(a, b)
    lcs_num = lcs.max_lcs()
    print(lcs_num)
    assert lcs_num == 4


def test0():
    a = "mitcmu"
    b = "mtacnux"
    lcs = LongestCommonSequence(a, b)
    lcs_num = lcs.max_lcs()
    print(lcs_num)
    assert lcs_num == 4


def test1():
    a = "mitcmux"
    b = "mtacnu"
    lcs = LongestCommonSequence(a, b)
    lcs_num = lcs.max_lcs()
    print(lcs_num)
    assert lcs_num == 4


if __name__ == '__main__':
    test()
