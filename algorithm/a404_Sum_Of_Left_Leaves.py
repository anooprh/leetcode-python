import os


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        ans = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            ans += root.left.val
        ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    l1 = TreeNode(9)
    r1 = TreeNode(20, TreeNode(15), TreeNode(7))
    root = TreeNode(3, l1, r1)
    assert Solution().sumOfLeftLeaves(root) == 24
    print(" ---> Success")
