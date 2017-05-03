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
            ans = (len(s) > 0 and (s[-1] == p[-1] or '.' == p[-1]) and self.isMatch(s[:-1], p[:-1], table))
        else:
            ans = (((len(s) > 0 and (s[-1] == p[-2] or '.' == p[-2])) and (
                self.isMatch(s[:-1], p, table) or self.isMatch(s[:-1], p[:-2], table))) or self.isMatch(s, p[:-2],
                                                                                                        table))
        table[(s, p)] = ans
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s") == True
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("aa", ".*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True
    assert Solution().isMatch("abcd", "d*") == False
    assert Solution().isMatch("aaa", "ab*ac*a") == True
    assert Solution().isMatch("aaa", "aaaa") == False
    print(" ---> Success")
