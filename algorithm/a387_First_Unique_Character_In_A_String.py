import collections
import os


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = [0 for _ in range(26)]
        for c in s:
            seen[ord(c) - ord("a")] += 1
        for i,c in enumerate(s):
            if seen[ord(c) - ord("a")] == 1 : return i
        return -1

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
    print(" ---> Success")
