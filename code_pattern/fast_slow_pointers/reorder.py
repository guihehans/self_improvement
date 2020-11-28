"""
@author: guihehans
@file: reorder.py 
@time: 2020/11/28 20:35
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
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    if head is None or head.next is None:
        return head
    # 1 find mid
    # reverse 2nd half
    # loop 1st hf and 2nd half simultaneously,insert 2nd half one by one
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    head_second_half = reverse(slow)
    head_copy = head
    while head is not None and head_second_half is not None:
        if head_second_half.next is None:
            break
        head_2 = head_second_half.next
        tmp = head.next
        head.next = head_second_half
        head_second_half.next = tmp
        head = tmp
        head_second_half = head_2

    return head_copy


def reverse(head):
    if head is None or head.next is None:
        return head
    prev, cur = None, head
    while cur:
        next_p = cur.next
        cur.next = prev
        prev = cur
        cur = next_p
    return prev


def test_case_1():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


if __name__ == '__main__':
    test_case_1()
