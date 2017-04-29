import collections
import os


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        for c in c1:
            if c not in c2 or c2[c] < c1[c]: return False
        return True


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().canConstruct("a", "b") == False
    assert Solution().canConstruct("aa", "ab") == False
    assert Solution().canConstruct("aa", "aab") == True
    print(" ---> Success")
