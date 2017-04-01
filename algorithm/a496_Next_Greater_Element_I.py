import os


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        return [self.findOne(num, nums) for num in findNums]

    def findOne(self, num, nums):
        for i in range(nums.index(num) + 1, len(nums)):
            if nums[i] > num: return nums[i]
        return -1


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    print " ---> Success"
