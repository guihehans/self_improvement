"""
@author: guihehans
@file: knapsack_value.py 
@time: 2020/11/21 0:21
@function:

"""
import math


class KnapsackWithValue:
    def __init__(self, items, values, n, w):
        self.items = items
        self.values = values
        self.n = n
        self.w = w
        self.maxW = -math.inf
        self.maxV = -math.inf

    def f(self, i, cw, cv):
        if cw == self.w or i == self.n:
            # if cw > self.maxW:
            #     self.maxW = cw
            if cv > self.maxV:
                self.maxV = cv
            return
        # check item i not select condition,go to check i+1
        self.f(i + 1, cw, cv)
        # return from i+1 to i, now select item i
        if cw + self.items[i] <= self.w:
            self.f(i + 1, cw + self.items[i], cv + self.values[i])


def test_cast_1():
    items = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    n = len(items)
    w = 9
    knapsack = KnapsackWithValue(items, values, n, w)
    knapsack.f(0, 0, 0)
    print(knapsack.maxV)


if __name__ == '__main__':
    test_cast_1()
