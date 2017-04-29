import os


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None: return None
        if root.left is not None: root.left.next = root.right
        if root.right is not None: root.right.next = root.next.left if root.next is not None else None
        self.connect(root.left)
        self.connect(root.right)


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    #           5
    #         /  \
    #        4    8
    #       / \  / \
    #      11 3 13  4

    seven = TreeLinkNode(7)
    two = TreeLinkNode(2)
    eleven = TreeLinkNode(11, seven, two)
    three = TreeLinkNode(3)
    four = TreeLinkNode(4, eleven, three)
    thirteen = TreeLinkNode(13)
    one = TreeLinkNode(1)
    four2 = TreeLinkNode(4, None, one)
    eight = TreeLinkNode(8, thirteen, four2)
    root = TreeLinkNode(5, four, eight)
    Solution().connect(root)

    assert root.next == None
    assert four.next == eight and eight.next == None
    assert eleven.next == three and three.next == thirteen and thirteen.next == four2 and four2.next == None
    print(" ---> Success")
