import os
import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]w
        """
        l = bisect.bisect_left(nums, target)
        if l > (len(nums) - 1) or nums[l] != target:
            return [-1, -1]
        r = bisect.bisect_right(nums, target)
        return [l, r - 1]


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 9) == [-1, -1]
    assert Solution().searchRange([], 9) == [-1, -1]
    # Solution().searchRange([5, 7, 7, 8, 8, 10], 10) == [3, 4]
    # Solution().searchRange([5, 7, 7, 8, 8, 10], 9) == [-1, -1]
    print " ---> Success"
