import os

#  Not yet accepted

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, i = [], 0
        while True:
            x += map(int, list(str(i)))
            i += 1
            if len(x) > n: return x[n]


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().findNthDigit(11) == 0
    assert False
    print " ---> Success"
