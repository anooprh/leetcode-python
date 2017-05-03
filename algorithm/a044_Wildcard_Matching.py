import os


class Solution(object):
    def isMatch(self, s, p, table={}):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s, p) in table: return table[(s, p)]
        if p == '':
            ans = (s == '')
        elif p[-1] != '*':
            ans = (len(s) > 0 and (s[-1] == p[-1] or '?' == p[-1]) and self.isMatch(s[:-1], p[:-1], table))
        else:
            ans = self.isMatch(s, p[:-1], table) or (
                len(s) > 0 and ((self.isMatch(s[:-1], p[:-1], table)) or self.isMatch(s[:-1], p, table)))

        table[(s, p)] = ans
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isMatch("", "*") == True
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("aa", "*") == True
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("ab", "?*") == True
    assert Solution().isMatch("aab", "c*a*b") == False
    print(" ---> Success")
