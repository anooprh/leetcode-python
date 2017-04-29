import os
import collections
import bisect


class Solution(object):
    def binary_search(self, a, k, lo=0, hi=None):
        hi = hi if hi is not None else len(a)
        pos = bisect.bisect_left(a, k, lo, hi)
        return pos if pos != hi and a[pos] == k else -1

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        if k == 0:
            for k, v in collections.Counter(nums).items():
                if v > 1: ans += 1
        elif k > 0:
            nums.sort()
            for i, num in enumerate(nums):
                if i != 0 and nums[i] == nums[i - 1]: continue
                if self.binary_search(nums, num + k) != -1: ans += 1
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().findPairs([3, 1, 4, 1, 5], 2) == 2
    assert Solution().findPairs([1, 2, 3, 4, 5], 1) == 4
    assert Solution().findPairs([1, 3, 1, 5, 4], 0) == 1
    print(" ---> Success")
