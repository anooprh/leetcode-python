import os

import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd_seen = False
        ans = 0
        for v in collections.Counter(s).values():
            if not odd_seen and v%2 == 1:
                ans += v
                odd_seen = True
            else :
                ans += (v//2)*2
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().longestPalindrome('abccccdd') == 7
    print(" ---> Success")
