import os


class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prev = ListNode(0)
        head = prev
        sum = carry = 0
        while l1 is not None or l2 is not None:
            now = ListNode(0)
            sum = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
            now.val = sum % 10
            carry = sum // 10
            prev.next = now
            prev = now

            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        if carry is not 0: prev.next = ListNode(carry)
        return head.next

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    assert Solution().addTwoNumbers(l1, l2) == ListNode(7, ListNode(0, ListNode(8)))
    print(" ---> Success")
