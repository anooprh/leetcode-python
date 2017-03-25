import os


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for num in nums:
            if num is not 0:
                nums[pos] = num
                pos += 1

        for i in range(pos, len(nums)): nums[i] = 0
        pass


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]
    print " ---> Success"
