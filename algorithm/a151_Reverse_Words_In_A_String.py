import os


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"
    print(" ---> Success")
