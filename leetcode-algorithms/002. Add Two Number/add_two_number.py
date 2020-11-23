# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        while self.next:
            print(self.val)
            self = self.next
        print(self.val)


def init_List_from_array(l: list):
    tail_num = l[-1]
    tail = ListNode(tail_num)
    l.reverse()
    for num in l[1:]:
        temp = ListNode(num)
        temp.next = tail
        tail = temp
    return tail


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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


if __name__ == '__main__':
    test1, test2 = [2, 4, 3], [5, 6, 4]
    test1, test2 = [5], [5, 5]
    l1 = init_List_from_array(test1)
    l2 = init_List_from_array(test2)

    sol = Solution()
    print((10 / 10))
    result = sol.addTwoNumbers(l1, l2)
    result.print()
