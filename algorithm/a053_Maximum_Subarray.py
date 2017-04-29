import os


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = sum = 0
        if len(nums) == 0: return max_sum
        max_sum = sum = nums[0]
        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            if sum > max_sum: max_sum = sum
        return max_sum


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print(" ---> Success")
