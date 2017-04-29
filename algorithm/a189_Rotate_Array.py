import os


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[-k:] + nums[:-k]
        for i, t in enumerate(temp):
            nums[i] = t


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
    nums = [1, 2]
    Solution().rotate(nums, 3)
    assert nums == [2, 1]
    print(" ---> Success")
