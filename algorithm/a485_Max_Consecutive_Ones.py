import os

# Accepted but the solution is incorrect

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :typenums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            i = abs(num) - 1
            nums[i] = - abs(nums[i])

        return [i + 1 for (i, num) in enumerate(nums) if num > 0]


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().findDisappearedNumbers([1]) == []
    assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1, 1]) == [5, 6]
    print(" ---> Success")
