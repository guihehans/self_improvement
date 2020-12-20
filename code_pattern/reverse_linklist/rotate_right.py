#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: rotate_right.py
@time: 2020/12/9 17:23
@function:
Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
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


def rotate(head, k):
    if head is None or k == 0:
        return head
    cur = head
    n = 0
    while cur is not None:
        tail = cur
        cur = cur.next
        n += 1

    # find last node to rotate.
    m = k % n
    # if m==0, no need to rotate, return head.
    if m == 0:
        return head
    prev_tail = get_k_from_end(head, m + 1)
    k_node = prev_tail.next

    # break from prev_tail. insert from tail to prev linked list.
    prev_tail.next = None
    tail.next = head

    return k_node


def get_k_from_end(head: Node, k: int) -> Node:
    fast, slow = head, head
    for i in range(k):
        if fast is not None:
            fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


def test_1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 8)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


def test_2():
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 4)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


def test_3():
    head = Node(1)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 0)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


def test_4():
    head = Node(1)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 1)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


if __name__ == '__main__':
    test()
