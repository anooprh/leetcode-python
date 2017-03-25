import os


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().strStr("","") == 0
    assert Solution().strStr("","a") == -1
    print " ---> Success"
