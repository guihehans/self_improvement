"""
@author: guihehans
@file: levenshtein_dist.py 
@time: 2020/11/22 22:31
@function:
given 2 string with same length,
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
        self.mem = [[-1 for j in range(self.m)] for i in range(self.n)]

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
            if i < self.m - 1:
                edit_dist += self.m - 1 - i
            if j < self.n - 1:
                edit_dist += self.n - 1 - j
            if edit_dist < self.min_dist:
                self.min_dist = edit_dist
            return
        if self.a[i] == self.b[j]:
            self.lvst_dist(i + 1, j + 1, edit_dist)
        else:
            self.lvst_dist(i + 1, j, edit_dist + 1)
            self.lvst_dist(i, j + 1, edit_dist + 1)
            self.lvst_dist(i + 1, j + 1, edit_dist + 1)


def f():
    a = "mitcmu"
    b = "mtacnu"
    lv = LevenshteinDistance(a, b)
    lv.lvst_dist(0, 0, 0)
    print(lv.min_dist)


if __name__ == '__main__':
    f()
