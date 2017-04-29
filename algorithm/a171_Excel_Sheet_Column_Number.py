import collections
import os


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for c in s:
            ans *= 26
            ans += ord(c) - ord("A") + 1
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().titleToNumber("A") == 1
    assert Solution().titleToNumber("Z") == 26
    assert Solution().titleToNumber("AA") == 27
    assert Solution().titleToNumber("AB") == 28
    print(" ---> Success")
