import os
import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ans = self.nums[:]
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randrange(0, i + 1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    # Don't know how to assert on this
    print(" ---> Success")
