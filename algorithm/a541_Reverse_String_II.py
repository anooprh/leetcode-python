import os


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return ''.join([p[::-1] if j % 2 == 0 else p for j, p in enumerate([s[i:i + k] for i in range(0, len(s), k)])])


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().reverseStr('abcdefg', 2) == 'bacdfeg'
    print(" ---> Success")
