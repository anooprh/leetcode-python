import os


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n * (n + 1) / 2) - sum(nums)


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().missingNumber([0, 1, 3]) == 2
    print " ---> Success"
