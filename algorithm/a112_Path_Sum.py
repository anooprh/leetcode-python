import os


class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None: return False
        return sum == root.val if root.left is None and root.right is None else (
        self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val))


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    #          5
    #         / \
    #        4   8
    #       /   / \
    #      11  13  4
    #     /  \      \
    #    7    2      1
    l1 = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    r1 = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    root = TreeNode(5, l1, r1)
    assert Solution().hasPathSum(root, 22) == True
    print(" ---> Success")
