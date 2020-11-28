"""
@author: guihehans
@file: find_palindrome.py 
@time: 2020/11/28 16:24
@function:

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True
    # 1. find mid using fast,slow
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # 2. reverse the 2nd half from mid
    reversed_mid = reverse_list(slow)
    reversed_mid_copy = reversed_mid
    s_head = head
    while s_head and reversed_mid:
        if s_head.value != reversed_mid.value:
            break
        s_head = s_head.next
        reversed_mid = reversed_mid.next
    # reverse the 2nd half again to keep list complete
    reversed_mid_copy = reverse_list(reversed_mid_copy)
    if s_head is None or reversed_mid is None:
        return True
    else:
        return False


def reverse_list(head):
    if head is None or head.next is None:
        return head
    prev, cur = None, head
    while cur:
        next_p = cur.next
        cur.next = prev
        prev = cur
        cur = next_p
    return prev


def test_case_0():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    assert (is_palindromic_linked_list(head)) is True


def test_case_1():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(2)
    assert (is_palindromic_linked_list(head)) is False


def test_case_2():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(2)
    assert (is_palindromic_linked_list(head)) is True


def test_case_3():
    head = Node(1)
    head.next = Node(0)
    head.next.next = Node(0)
    assert (is_palindromic_linked_list(head)) is False


if __name__ == '__main__':
    test_case_0()
    test_case_1()
    test_case_2()
