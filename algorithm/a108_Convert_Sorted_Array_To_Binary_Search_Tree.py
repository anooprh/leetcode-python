import os


def checkSame(t1, t2):
    if t1 is None and t2 is None: return True

    return t1 and t2 and t1.val == t2.val and \
           checkSame(t1.left, t2.left) and checkSame(t1.right, t2.right)


class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(nums[0])
        mid = len(nums) / 2
        t = TreeNode(nums[mid])
        t.left = self.sortedArrayToBST(nums[0:mid])
        t.right = self.sortedArrayToBST(nums[mid + 1:])
        return t


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert checkSame(Solution().sortedArrayToBST([1, 2, 3, 4, 5]),
                     TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(5, TreeNode(4), None)))
    print " ---> Success"
