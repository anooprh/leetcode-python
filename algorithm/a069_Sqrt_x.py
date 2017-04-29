import os


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**0.5)

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(9) == 3
    assert Solution().mySqrt(10) == 3
    print(" ---> Success")
