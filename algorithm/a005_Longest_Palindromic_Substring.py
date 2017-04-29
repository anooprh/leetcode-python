import os


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            odd = self.expand_odd(s, i)
            if len(odd) > len(ans): ans = odd

        for i in range(len(s)-1):
            even = self.expand_even(s, i)
            if len(even) > len(ans): ans = even

        return ans

    def expand_odd(self, s, i):
        st, en = i, i
        while True:
            if st == 0 or en == len(s) - 1: break
            if not s[st - 1] == s[en + 1]: break
            st -= 1
            en += 1
        return s[st:en + 1]

    def expand_even(self, s, i):
        st, en = i+1, i
        while True:
            if st == 0 or en == len(s) - 1: break
            if not s[st - 1] == s[en + 1]: break
            st -= 1
            en += 1
        return s[st:en + 1]


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().longestPalindrome("babad") == "bab"
    assert Solution().longestPalindrome("cbbd") == "bb"
    print(" ---> Success")
