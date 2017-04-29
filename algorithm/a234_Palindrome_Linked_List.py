import os


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = self.find_len(head)
        if l <= 1: return True
        (l1, e1) = self.get_first_part(head, 0, l // 2 - 1)
        l2 = self.get_second_part(head, l // 2 + 1 if l % 2 == 1 else l // 2, l - 1)
        e1.next = None
        return self.check_same(l1, l2)

    def find_len(self, head):
        ans = 0
        while head != None:
            head = head.next
            ans += 1
        return ans

    def get_second_part(self, head, s, e):
        n, start = head, None
        for i in range(s - 1):
            n = n.next
        start = n.next
        n.next = None

        return self.reverse_ll(start)

    def reverse_ll(self, node):
        if node.next is None:
            return node
        e = node.next
        node.next = None
        s = self.reverse_ll(e)
        e.next = node
        return s

    def get_first_part(self, head, s, e):
        n = head
        for i in range(e):
            n = n.next
        return (head, n)

    def check_same(self, l1, l2):
        while l1 != None and l2 != None:
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next

        return l1 == l2


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isPalindrome(None) == True
    assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))) == True
    assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(1)))))) == False
    assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))) == True
    assert Solution().isPalindrome(
        ListNode(1, ListNode(4, ListNode(-1, ListNode(-1, ListNode(4, ListNode(1))))))) == True
    assert Solution().isPalindrome(
        ListNode(1, ListNode(4, ListNode(-1, ListNode(-1, ListNode(-1, ListNode(4, ListNode(1)))))))) == True
    assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(3))))) == False
    print(" ---> Success")
