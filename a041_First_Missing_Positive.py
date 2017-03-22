import os


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        table = [False for _ in range(max(nums))]
        for num in nums:
            if num > 0: table[num - 1] = True
        for i, _ in enumerate(table):
            if not table[i]: return i + 1
        return len(table) + 1


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().firstMissingPositive([1, 2, 0]) == 3
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2
    assert Solution().firstMissingPositive([]) == 1
    assert Solution().firstMissingPositive([3, 2]) == 1
    assert Solution().firstMissingPositive([1000, -1]) == 1
    assert Solution().firstMissingPositive([1000, 1]) == 2
    print " ---> Success"
