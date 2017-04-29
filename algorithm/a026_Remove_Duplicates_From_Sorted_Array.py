import os


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        (ans, prev) = (1, nums[0]) if len(nums) > 0 else (0, None)
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[ans] = nums[i]
                ans += 1
            prev = nums[i]
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    l1 = [1, 1, 5]
    assert Solution().removeDuplicates(l1) == 2
    assert l1 == [1, 5, 5]
    assert Solution().removeDuplicates([1, 3, 5]) == 3
    print(" ---> Success")
