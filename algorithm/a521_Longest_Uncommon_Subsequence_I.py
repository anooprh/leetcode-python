import os


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return max(len(a), len(b)) if a != b else -1


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().findLUSlength('aba', 'cdc') == 3
    print(" ---> Success")
