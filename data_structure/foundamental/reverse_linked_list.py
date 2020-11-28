"""
@author: guihehans
@file: reverse_linked_list.py 
@time: 2020/11/28 15:29
@function:

reverse a singly LinkedList, at O(1) space and O(N) time.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    prev = None
    cur = head

    while cur:
        next_p = cur.next
        cur.next = prev
        prev = cur
        cur = next_p

    return prev


def test_empty():
    head = Node(1)
    assert reverse_linked_list(head).value == 1


def test_case1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    assert reverse_linked_list(head).value == 5
