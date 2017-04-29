import os


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count('1') == 1


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isPowerOfTwo(25) == False
    assert Solution().isPowerOfTwo(16) == True
    print(" ---> Success")
