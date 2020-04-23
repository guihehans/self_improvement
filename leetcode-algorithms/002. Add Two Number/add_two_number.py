# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        curr = result
        inc = 0
        p, q = l1, l2
        while (p or q):
            x = p.val if (p) else 0
            y = q.val if (q) else 0
            sum = x + y + inc
            inc, re = divmod(sum, 10)
            curr.next = ListNode(re)
            curr = curr.next
            if (p):
                p = p.next
            if (q):
                q = q.next
        if inc > 0:
            curr.next = ListNode(inc)

        return result.next
