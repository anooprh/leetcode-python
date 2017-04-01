import os


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count("1")


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().hammingDistance(1, 4) == 2
    print " ---> Success"
