import os

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = set()
        for num in nums:
            if num in table: table.remove(num)
            else: table.add(num)
        for e in table: return e

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().singleNumber([1,2,3,2,3]) == 1
    print(" ---> Success")
