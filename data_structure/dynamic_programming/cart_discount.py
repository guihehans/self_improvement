"""
@author: guihehans
@file: cart_discount.py
@time: 2020/11/21 0:15
@function:
the cart problem
problem description:
the shop has a discount event, total cart value >=200,minus 50.
assume cart items numbers n>100.
try to get which items should buy when satisfy the discount condition,will
lead to total value most close to 200.

"""


def find_cart_items(items, n, max_value, condition_value):
    assert condition_value <= max_value
    # init 2d states array [n][max_value]
    states = [[False for j in range(max_value + 1)] for i in range(n)]
    # init stage 1,first item
    states[0][0] = True
    if items[0] <= max_value:
        states[0][items[0]] = True

    for i in range(1, n):
        for j in range(max_value + 1):
            if states[i - 1][j]:  # not picking items[i]
                states[i][j] = True
        for j in range(max_value + 1 - items[i]):
            if states[i - 1][j]:  # picking items[i]
                states[i][j + items[i]] = True

    # get min value closest to condition_value
    min_value = 0
    for i in range(condition_value, max_value + 1):
        if states[n - 1][i]:
            min_value = i
            break

    # now backtracking the items.
    cur_value = min_value
    for i in range(n - 1, 0, -1):
        if cur_value - items[i] >= 0 and states[i - 1][cur_value - items[i]]:
            print("items:{}, price:{} is bought".format(i, items[i]))
            cur_value -= items[i]

    if cur_value != 0:
        i = 0
        print("items:{}, price:{} is bought".format(i, items[i]))
