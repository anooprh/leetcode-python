import os


class TreeNode(object):
    def __init__(self, x,l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def asList(self, root):
        if root is None:
            return []
        else:
            return [root.val] + self.asList(root.left) + self.asList(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = sorted(self.asList(root))
        return min([abs(n - l[i]) for i, n in enumerate(l[1:])])


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().getMinimumDifference(TreeNode(1, None, TreeNode(3, TreeNode(2), None))) == 1
    print(" ---> Success")
