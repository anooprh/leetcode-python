import os


# The isBadVersion API is already defined for you.
# @param
# version, an integer
# @ return a bool
def isBadVersion(version):
    return version >= THRESHOLD  # In this test case, 7 is the first bad version


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        st = 0
        en = n
        while en > st:
            if isBadVersion(en) and (en == st or not isBadVersion(en - 1)): return en
            if isBadVersion(en):
                en = st + (en - st) / 2
            else:
                st, en = en, en + (en - st) / 2 + 1


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    for THRESHOLD in range(1,10):
        assert Solution().firstBadVersion(10) == THRESHOLD
    print " ---> Success"
