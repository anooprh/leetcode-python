import os


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().reverseString("hello") == "olleh"
    print(" ---> Success")
