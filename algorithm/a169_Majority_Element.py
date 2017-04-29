import os


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        for num in nums:
            table[num] = table[num] + 1 if num in table else 1
        for num in table:
            if table[num] > len(nums) / 2: return num
        return None


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().majorityElement([1, 1, 5]) == 1
    print(" ---> Success")
