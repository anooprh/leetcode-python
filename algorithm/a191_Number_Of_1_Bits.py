import os


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().hammingWeight(1) == 1
    assert Solution().hammingWeight(2) == 1
    assert Solution().hammingWeight(3) == 2
    assert Solution().hammingWeight(11) == 3
    print(" ---> Success")
