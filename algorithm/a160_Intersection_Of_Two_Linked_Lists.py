import os


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        (l1, e1) = self.get_prop(headA)
        (l2, e2) = self.get_prop(headB)

        if e1 != e2 or (e1 == None and e2 == None):
            return None
        (headA_new, headB_new) = (headA, headB)
        if l1 > l2:
            headA_new = self.adv(headA, l1 - l2)
        else:
            headB_new = self.adv(headB, l2 - l1)

        while headA_new.val != headB_new.val:
            headA_new = headA_new.next
            headB_new = headB_new.next
        return headA_new

    def get_prop(self, head):
        l = 0
        prev = None
        while head != None:
            l += 1
            prev = head
            head = head.next
        return (l, prev)

    def adv(self, head, n):
        for i in range(n):
            head = head.next
        return head


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    c = ListNode("c1", ListNode("c2", ListNode("c3")))
    l1 = ListNode("a1", ListNode("a2", c))
    l2 = ListNode("b1", ListNode("b2", ListNode("b3", c)))
    assert Solution().getIntersectionNode(l1, l2) == c
    print " ---> Success"
