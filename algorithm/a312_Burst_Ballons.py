import os


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1: return 0
        T = [[0 for _ in nums] for _ in nums]
        for length in range(1,len(nums)+1):
            for i in range(len(nums)-length+1):
                j = i + length - 1
                best = 0
                for k in range(i,j+1):
                    left = (T[i][k-1] if k > i else 0)
                    right = (T[k+1][j] if k < j else 0)
                    center = (nums[k] * (nums[i-1] if i > 0 else 1) * (nums[j+1] if j < len(nums)-1 else 1) )
                    best = max(best, left+right+center)
                T[i][j] = best
        return T[0][len(nums)-1]

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().maxCoins([3,1,5,8]) == 167
    print(" ---> Success")
