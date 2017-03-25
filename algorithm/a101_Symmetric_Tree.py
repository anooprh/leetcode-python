import os


class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSymmetric_internal(root, root)

    def isSymmetric_internal(self, l, r):

        if not l and not r: return True
        if l and r and l.val == r.val:
            return self.isSymmetric_internal(l.left, r.right) and self.isSymmetric_internal(l.right, r.left)
        return False


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                                           TreeNode(2, TreeNode(4), TreeNode(3)))) == True
    assert Solution().isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)),
                                           TreeNode(2, None, TreeNode(3)))) == False
    print " ---> Success"
