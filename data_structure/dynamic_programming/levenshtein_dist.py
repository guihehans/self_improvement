"""
@author: guihehans
@file: levenshtein_dist.py 
@time: 2020/11/22 22:31
@function:
There're 2 string: a,b with length n,m.
the minimal operation takes to make 2 strings equal is their levenshtein distance.
the operation is insertion,deletion,substitution.

"""
import math


class LevenshteinDistance:
    def __init__(self, a: str, b: str):
        self.a = a
        self.b = b
        self.n = len(a)
        self.m = len(b)
        self.min_dist = math.inf

    def lvst_dist(self, i, j, edit_dist):
        """
        recursive method.
        :param i:
        :param j:
        :param edit_dist:
        :return:
        """
        # termination
        if i == self.n - 1 or j == self.m - 1:
            # note n can be different from m. the diff should be add to edit dist.
            if i < self.m - 1:
                edit_dist += self.m - 1 - i
            if j < self.n - 1:
                edit_dist += self.n - 1 - j
            # update the min_dist
            if edit_dist < self.min_dist:
                self.min_dist = edit_dist
            return
        if self.a[i] == self.b[j]:
            self.lvst_dist(i + 1, j + 1, edit_dist)
        else:
            self.lvst_dist(i + 1, j, edit_dist + 1)
            self.lvst_dist(i, j + 1, edit_dist + 1)
            self.lvst_dist(i + 1, j + 1, edit_dist + 1)

    def lvst_dist_dp(self):
        """
        solve levenshtein dist with dp.
        1.set up states formula.
        min_dist(i,j)=min{min_dist(i-1,j)+1,min_dist(i,j-1)+1,min_dist(i-1,j-1)} if a[i]==b[j]
                    =min{min_dist(i-1,j)+1,min_dist(i,j-1)+1,min_dist(i-1,j-1)+1} if a[i]!=b[j]
        2. set up states transform array.
        states[n][m]. states[i][j] stores the min_dist[i.j]
        for convenience, write the value row by row.

        :param i:
        :param j:
        :return:
        """
        # the states is [n][m] 0:m at in a row, 0:t in a col.
        states = [[-1 for j in range(self.m)] for i in range(self.n)]
        n, m = self.n, self.m
        a, b = self.a, self.b
        # set up row 0.
        for j in range(m):
            # 只要当前字符相等,无论比较的长度是多少,min_dist都是j。
            if a[0] == b[j]:
                states[0][j] = j
            # 不相等要分情况,依据状态公式来
            elif j == 0:
                states[0][j] = 1
            else:
                states[0][j] = states[0][j - 1] + 1
        # set up col 0
        for i in range(n):
            if a[i] == b[0]:
                states[i][0] = i
            elif i == 0:
                states[i][0] = 1
            else:
                states[i][0] = states[i - 1][0] + 1

        # now fill the rest of states[i][j]
        for i in range(1, n):
            for j in range(1, m):
                if a[i] == b[j]:
                    states[i][j] = min(states[i - 1][j] + 1, states[i][j - 1] + 1, states[i - 1][j - 1])
                else:
                    states[i][j] = min(states[i - 1][j] + 1, states[i][j - 1] + 1, states[i - 1][j - 1] + 1)

        return states[n - 1][m - 1]


def test():
    a = "mitcmu"
    b = "mtacnuc"
    lv = LevenshteinDistance(a, b)
    lv.lvst_dist(0, 0, 0)
    assert 4 == lv.min_dist


def test_1():
    a = "mitcmu"
    b = "mtacnu"
    lv = LevenshteinDistance(a, b)
    min_dist = lv.lvst_dist_dp()
    assert 3 == min_dist


def test_2():
    a = "mtacnux"
    b = "mitcmu"
    lv = LevenshteinDistance(a, b)
    min_dist = lv.lvst_dist_dp()
    assert 4 == min_dist


if __name__ == '__main__':
    test()
    test_1()
    test_2()
