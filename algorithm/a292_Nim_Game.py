import os


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not n % 4 == 0


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().canWinNim(4) == False
    assert Solution().canWinNim(3) == True
    print(" ---> Success")
