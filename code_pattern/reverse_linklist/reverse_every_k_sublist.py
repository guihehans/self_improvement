#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: reverse_every_k_sublist.py
@time: 2020/12/8 16:45
@function:

"""

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements(head, k):
    prev, cur = None, head
    while cur is not None:
        i = 1
        start = cur
        while cur is not None and i <= k:
            tail = cur
            cur = cur.next
            i += 1

        if i == k + 1:
            tail_next = cur
            reversed_start, reversed_tail = reverse(start, tail)
            # insert pre
            if prev is None:
                head = reversed_start
            if prev is not None:
                prev.next = reversed_start
            # insert tail
            reversed_tail.next = tail_next
            # update prev
            prev = reversed_tail

    return head


def reverse(start, tail):
    prev, cur, tail_next = None, start, tail.next
    while cur is not None and cur != tail_next:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev, start


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    # TODO: fix unit test
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


def test_1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 8)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


def test_2():
    head = Node(1)
    head.next = Node(2)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


if __name__ == '__main__':
    test()
