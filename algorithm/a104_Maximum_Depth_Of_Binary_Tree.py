import os


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype:
        """
        return 0 if root is None else (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    assert Solution().maxDepth(root) == 3
    assert Solution().maxDepth(None) == 0
    print(" ---> Success")
