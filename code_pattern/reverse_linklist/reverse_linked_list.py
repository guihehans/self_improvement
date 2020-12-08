#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: reverse_linked_list.py
@time: 2020/12/8 14:05
@function:
Given the head of a Singly LinkedList, reverse the LinkedList.
Write a function to return the new head of the reversed LinkedList.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur is not None:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_

        return prev


