#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: reverse_sub_list.py
@time: 2020/12/8 14:40
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


def reverse_sub_list(head, p, q):
    """
    assume head is at pos 1.
    iterate and record current index. reverse between p a
    :param head:
    :param p:
    :param q:
    :return:
    """
    # as long as p==q, no reverse. otherwise there must be a reverse.
    if p == q:
        return head
    index = 1

    prev, cur = None, head
    prev_node, reverse_head = None, head

    while cur and index <= q:
        if index < p:
            prev_node = cur
            cur = cur.next
            reverse_head = cur
        elif p <= index <= q:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        index += 1

    # link the prev_node to reversed head,prev
    if prev_node is not None:
        prev_node.next = prev
    else:
        head = prev
    # link the reversed head, to the left tail, cur
    reverse_head.next = cur

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    i = 1
    cur = head
    while cur is not None:
        assert cur.value == i
        cur = cur.next
        i += 1

    result = reverse_sub_list(head, 2, 4)
    items = [1, 4, 3, 2, 5]
    i = 0
    while i < len(items) and result is not None:
        assert result.value == items[i]
        result = result.next
        i += 1


def test_null():
    head = Node(1)

    result = reverse_sub_list(head, 1, 1)
    assert result is head


def test_s():
    head = Node(3)
    head.next = Node(5)
    result = reverse_sub_list(head, 1, 2)
    items = [5, 3]
    i = 0
    while i < len(items) and result is not None:
        assert result.value == items[i]
        result = result.next
        i += 1


def test_1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    result = reverse_sub_list(head, 1, 2)
    items = [2, 1, 3]
    i = 0
    while i < len(items) and result is not None:
        assert result.value == items[i]
        result = result.next
        i += 1


if __name__ == '__main__':
    test()
