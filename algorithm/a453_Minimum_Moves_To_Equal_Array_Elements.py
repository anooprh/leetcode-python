import os


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        m = min(nums)
        for num in nums:
            ans += num - m
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().minMoves([1,2,3]) == 3
    print(" ---> Success")
