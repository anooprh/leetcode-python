import os


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        for i,n in enumerate(numbers):
            if target - n in t:return [t[target-n]+1,i+1]
            else: t[n] = i


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1,2]
    print(" ---> Success")
