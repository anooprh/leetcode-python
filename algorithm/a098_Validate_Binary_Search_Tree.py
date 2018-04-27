import os


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def isValidBST(self, root, lb=-float('inf'), ub=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        if root.val <= lb or root.val >= ub: return False
        return self.isValidBST(root.left, lb, max(ub, root.val)) and self.isValidBST(root.right, min(lb, root.val), ub)


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isValidBST(TreeNode(1, TreeNode(1))) == False
    print(" ---> Success")
