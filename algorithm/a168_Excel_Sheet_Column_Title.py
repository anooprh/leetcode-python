import os


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n > 0:
            n -= 1
            ans = chr(ord('A') + (n) % 26) + ans
            n /= 26
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().convertToTitle(1) == "A"
    assert Solution().convertToTitle(2) == "B"
    assert Solution().convertToTitle(26) == "Z"
    assert Solution().convertToTitle(27) == "AA"
    assert Solution().convertToTitle(28) == "AB"
    print " ---> Success"
