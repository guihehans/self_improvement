"""
@author: guihehans
@file: coin_change.py 
@time: 2020/11/22 17:05
@function:

assume we got n kind of coins
need to pay w in total.
try to find the minimal numbers of coins can be used.
e.g.
coins=[1,3,5],w=9. min_num=3{3*3 or 1,3,5}

"""
import math


class CoinChange:
    def __init__(self, arr, to_pay):
        self.coins = arr
        self.to_pay = to_pay

    def min_coin(self, to_pay):
        """
        Min_coin(w)=1+min(min_coin(w-1),min_coin(w-3),min_coin(w-5))
        Min_coin[coins[i]]=1
        min_coin[w<0] =inf

        :param to_pay:
        :return:
        """
        if to_pay in self.coins:
            return 1
        elif to_pay < 1:
            return math.inf

        list_param = [to_pay - x for x in self.coins]
        min_num = 1 + min(map(self.min_coin, list_param))
        return min_num


def f():
    coins = [1, 3, 5]
    w = 9
    coin_change = CoinChange(coins, w)
    c = coin_change.min_coin(w)
    print(c)


def f_1():
    coins = [1, 2, 3, 5]
    w = 9
    coin_change = CoinChange(coins, w)
    c = coin_change.min_coin(w)
    print(c)


if __name__ == '__main__':
    f()
    f_1()
