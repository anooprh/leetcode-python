import os

class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for i, num in enumerate(nums):
            if target - num in m:
                return [m[target - num], i]
            else:
                m[num] = i

if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().twoSum([1, 3, 5], 8) == [1, 2]
    print " ---> Success"
