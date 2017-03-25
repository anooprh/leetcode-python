import os


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        if head is not None: fast = head.next
        else: return False
        while fast is not None and fast.next is not None:
            if fast == slow: return True
            slow = slow.next
            fast = fast.next.next
        return False


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    node = ListNode(3)
    l1 = ListNode(1, ListNode(2, node))
    node.next = l1
    l2 = ListNode(1,ListNode(2, ListNode(4)))
    assert Solution().hasCycle(l1) == True
    assert Solution().hasCycle(l2) == False
    print " ---> Success"
