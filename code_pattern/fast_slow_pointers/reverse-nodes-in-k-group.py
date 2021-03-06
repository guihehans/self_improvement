"""
@author: guihehans
@file: reverse-nodes-in-k-group.py 
@time: 2020/11/29 1:30
@function:

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head, tail):
    """
    reverse the sub list, given it's head and tail.
    e.g, 1->2->3  =>   2->1->3  return Node(2) Node(1)
    :param head:
    :param tail:
    :return: the reverse sub list's head and tail
    """
    # TRICKY fist pre set to the head's next, which is tail.next
    # but in fact it doesnt matter, since we will concat in main function
    pre = tail.next
    # save copy
    head_copy = head
    tail_next=tail.next
    while head != tail_next: # stop when head reach original tail.next
        nex = head.next
        head.next = pre
        pre = head
        head = nex
    return tail, head_copy


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # set a dummy to be head's prev
        dummy = ListNode(0)
        # dummy next saves the head
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            # 走k步 若提前走到尾，返回头节点dummy.next
            for i in range(k):
                tail = tail.next
                if tail is None:
                    return dummy.next
            nex = tail.next
            head, tail = reverse(head, tail)
            # concat prev,nex
            pre.next = head
            tail.next = nex
            # reset head, pre.
            pre = tail
            head = tail.next
        return dummy.next


def test():
    soluton = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    reversed_head = soluton.reverseKGroup(head, k=2)
    assert 2 == reversed_head.val

if __name__ == '__main__':
    test()
