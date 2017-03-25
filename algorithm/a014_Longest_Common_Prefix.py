import os


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        (ans, a_s) = (len(strs[0]), strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < ans: (ans, a_s) = (len(strs[i]), strs[i])
            for j, pair in enumerate(zip(strs[i - 1], strs[i])):
                if j > ans: break
                if pair[0] != pair[1]:
                    ans = min(ans, j)
                    a_s = strs[i][:j]
        return a_s


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().longestCommonPrefix(["abc123", "abd", "ab"]) == "ab"
    assert Solution().longestCommonPrefix(["aa", "a"]) == "a"
    assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
    print " ---> Success"
