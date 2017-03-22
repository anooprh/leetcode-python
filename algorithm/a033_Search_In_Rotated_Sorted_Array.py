import os
import bisect

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        co = len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]: co = i - 1
        k = bisect.bisect_left(nums, target, 0, co + 1)
        if k < len(nums) and nums[k] == target: return k
        k = bisect.bisect_left(nums, target, co + 1, len(nums))
        if k < len(nums) and nums[k] == target: return k

        return -1


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 6) == 2
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 9) == -1
    print " ---> Success"
