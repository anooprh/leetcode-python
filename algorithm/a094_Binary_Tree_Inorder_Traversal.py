import os


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))) == [1, 3, 2]
    print(" ---> Success")
