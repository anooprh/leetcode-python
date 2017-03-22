import os


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return a + b


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().getSum(2, 3) == 5
    print " ---> Success"
