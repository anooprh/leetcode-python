import os


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


def check_same(l1, l2):
    while l1 != None and l2 != None:
        if l1.val != l2.val:
            return False
        l1, l2 = l1.next, l2.next

    return l1 == l2


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        e = head.next
        head.next = None
        s = self.reverseList(e)
        e.next = head
        return s


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert check_same(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), \
                      ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))

    print " ---> Success"
