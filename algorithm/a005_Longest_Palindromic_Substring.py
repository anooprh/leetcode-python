import os

# Not Accepted Yet

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = {}
        st, en, ans = 0, 0, ""
        for i, c in enumerate(s):
            if c not in table:
                table[c] = i
            else:
                if en - st > len(ans): ans = s[st:en + 1]
                st += 1
                table[c] = i


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().longestPalindrome("babad") == "bab"
    assert Solution().longestPalindrome("cbbd") == "bb"
    print " ---> Success"
