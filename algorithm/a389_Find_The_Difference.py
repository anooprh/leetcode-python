import os


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for c in s:
            d[c] = 1 if c not in d else d[c] + 1
        for c in t:
            if c not in d: return c
            if d[c] == 1:
                del d[c]
            else:
                d[c] -= 1


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().findTheDifference("abcd", "abcde") == "e"
    print(" ---> Success")
