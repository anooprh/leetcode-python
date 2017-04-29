import os


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type table: str
        :rtype: bool
        """
        table = {}
        for c in s:
            table[c] = table[c] + 1 if c in table else 1
        for c in t:
            if c not in table or table[c] <= 0: return False
            table[c] -= 1
            if table[c] == 0: del table[c]

        return len(table) == 0


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isAnagram("anagram", "nagaram") == True
    assert Solution().isAnagram("rat", "car") == False
    print(" ---> Success")
