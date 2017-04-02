import os


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def checkSame(t1, t2):
    if t1 is None:
        return t2 is None
    if t2 is None:
        return t1 is None
    return t1.val == t2.val and checkSame(t1.left, t2.left) and checkSame(t1.right, t2.right)


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            t = root.left
            root.left= self.invertTree(root.right)
            root.right = self.invertTree(t)

        return root


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    t1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    t2 = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
    assert checkSame(Solution().invertTree(t1), t2)
    print " ---> Success"
