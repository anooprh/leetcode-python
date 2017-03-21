import os


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m = {}
        st = ans = 0
        for i, c in enumerate(s):
            if c in m:
                ans = max(ans, i - st)
                st = max(st, m[c] + 1)
            m[c] = i
        ans = max(len(s) - st, ans)
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3  # abc
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1  # b
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3  # wke
    assert Solution().lengthOfLongestSubstring("abba") == 2
    assert Solution().lengthOfLongestSubstring("c") == 1
    assert Solution().lengthOfLongestSubstring("aab") == 2
    print " ---> Success"
