import os


def check_same(l1, l2):
    while l1 != None and l2 != None:
        if l1.val != l2.val:
            return False
        l1, l2 = l1.next, l2.next

    return l1 == l2


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = head = ListNode(-1)
        while l1 != None and l2 != None:
            (s.next, l1, l2) = (l1, l1.next, l2) if l1.val < l2.val else (l2, l1, l2.next)
            s = s.next
        if l1 == None:
            s.next = l2
        if l2 == None:
            s.next = l1
        return head.next


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')

    assert check_same(Solution().mergeTwoLists(ListNode(1, ListNode(3, ListNode(5))),
                                               ListNode(2, ListNode(4, ListNode(6)))),
                      ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(" ---> Success")
