import os


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.rob_int(nums, 0, {})

    def rob_int(self, nums, start, table):
        if start in table: return table[start]

        if nums is None or start >= len(nums):
            ans = 0
        else:
            ans = max(nums[start] + self.rob_int(nums, start + 2, table),
                      self.rob_int(nums, start + 1, table))

        table[start] = ans

        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().rob([1]) == 1
    assert Solution().rob([1, 2, 3]) == 4
    assert Solution().rob([2, 3, 2]) == 4
    print(" ---> Success")
