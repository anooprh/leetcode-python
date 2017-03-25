import os

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next != None:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None

if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    # This cannot be tested I believe
    print " ---> Success"
