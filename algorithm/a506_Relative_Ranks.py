import os


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = [''] * len(nums)
        t = sorted([(n, i) for i, n in enumerate(nums)], key=lambda x: -x[0])
        if len(nums) > 0: ans[t[0][1]] = "Gold Medal"
        if len(nums) > 1: ans[t[1][1]] = "Silver Medal"
        if len(nums) > 2: ans[t[2][1]] = "Bronze Medal"
        for i, pair in enumerate(t[3:]):
            ans[pair[1]] = str(i + 4)
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().findRelativeRanks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    print(" ---> Success")
