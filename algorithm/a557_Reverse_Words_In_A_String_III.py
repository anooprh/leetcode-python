import os


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x : x[::-1], s.split(' ')))

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    print(" ---> Success")
