import os
from functools import reduce


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.s = reduce(lambda s, n: s + [s[-1] + n], nums, [0])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.s[j + 1] - self.s[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    array = NumArray([-2, 0, 3, -5, 2, -1])
    assert array.sumRange(0, 2) == 1
    assert array.sumRange(2, 5) == -1
    assert array.sumRange(0, 5) == -3
    print(" ---> Success")
