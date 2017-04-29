import os


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None: return True
        if p is None and q is not None: return False
        if p is not None and q is None: return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    t1 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    t2 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    assert Solution().isSameTree(t1, t2) == True
    assert Solution().isSameTree(t1, None) == False
    print(" ---> Success")
