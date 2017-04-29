import os


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = [1, nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[-1] * nums[i])

        for i in range(len(nums) - 2, -1, -1):
            nums[i] = nums[i + 1] * nums[i]
        nums.append(1)
        for i in range(len(ans) - 1, 0, -1):
            ans[i] = ans[i - 1] * nums[i]
        return ans[1:]


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    # This cannot be tested I believe
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    print(" ---> Success")
