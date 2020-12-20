#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: reverse_alternating_k_sublist.py
@time: 2020/12/9 11:01
@function:
Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
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


def reverse_alternate_k_elements(head, k):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    tail = dummy
    start = head
    index = 1
    while start is not None:
        for i in range(k):
            tail_before = tail
            tail = tail.next
            if tail is None:
                start, tail = reverse(start, tail_before)
                prev.next = start
                return dummy.next

        tail_next = tail.next
        if index % 2 == 1:
            start, tail = reverse(start, tail)
            prev.next = start
            tail.next = tail_next
        prev = tail
        start = tail_next
        index += 1
    return dummy.next


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
    head.next.next.next.next.next.next.next.next = Node(9)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
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
    result = reverse_alternate_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


if __name__ == '__main__':
    test()
