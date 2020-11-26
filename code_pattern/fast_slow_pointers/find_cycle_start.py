#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_cycle_start.py
@time: 2020/11/26 15:12
@function:

"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle_length = find_cycle_length(slow)
                fast, slow, pos = head, head, 0
                for i in range(cycle_length):
                    if fast is not None:
                        fast = fast.next

                while fast != slow and fast is not None and slow is not None:
                    fast = fast.next
                    slow = slow.next
                    pos += 1
                return pos
        return -1


def find_cycle_length(slow: ListNode) -> int:
    cur = slow
    length = 0
    while True:
        cur = cur.next
        length += 1
        if cur == slow:
            break
    return length


def find_cycle_start(head: ListNode) -> ListNode:
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            cycle_length = find_cycle_length(slow)
            fast, slow, pos = head, head, 0
            for i in range(cycle_length):
                if fast is not None:
                    fast = fast.next

            while fast != slow and fast is not None and slow is not None:
                fast = fast.next
                slow = slow.next
                pos += 1
            return slow
    return None


def test_0():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


def test_1():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    head.next.next.next.next.next.next = head.next.next
    solution = Solution()
    assert 2 == solution.detectCycle(head)


if __name__ == '__main__':
    test_0()
    test_1()
