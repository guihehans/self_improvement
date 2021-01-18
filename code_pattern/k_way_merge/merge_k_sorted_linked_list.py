#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: merge_k_sorted_linked_list.py
@time: 2021/1/18 10:45
@function:

"""

from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(lists):
    resultHead = None

    n = len(lists)
    if n == 0:
        return None
    elif n == 1:
        return lists[0]

    min_heap = []
    for i in range(len(lists)):
        head = lists[i]
        if head:
            heappush(min_heap, (head.val, i, head))

    cur_node = resultHead
    while min_heap:
        value, idx, head = heappop(min_heap)
        if not cur_node:
            cur_node = head
            resultHead = head
        else:
            cur_node.next = head
            cur_node = cur_node.next
        # push popped index's next node
        next_node = head.next
        if next_node:
            heappush(min_heap, (next_node.val, idx, next_node))
            next_node = next_node.next

    return resultHead


def test():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.val) + " ", end='')
        result = result.next


def test_1():
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.val) + " ", end='')
        result = result.next


if __name__ == '__main__':
    test()
