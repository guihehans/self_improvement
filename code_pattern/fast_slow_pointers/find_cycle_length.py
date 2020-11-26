#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_cycle_length.py
@time: 2020/11/26 14:26
@function:
use fast and slow pointer, given a cycle LinkedList, find the cycle length.
idea: first use slow fast to meet.
from meet point cur,use another pointer to traverse. when cur catch slow, the numbers of nodes traversed
is the circle length
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def find_cycle_length(node: Node) -> int:
    fast, slow = node, node
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            length = calculate_cycle_length(slow)
            return length


def calculate_cycle_length(slow: Node) -> int:
    cur = slow
    length = 0
    while True:
        cur = cur.next
        length += 1
        if cur == slow:
            break
    return length


def test():
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = head.next.next.next
    length = find_cycle_length(head)
    print(length)
    assert 2 == length


def test_2():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


if __name__ == '__main__':
    test()
    test_2()
