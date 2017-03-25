import os


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        positive = True
        if x < 0:
            positive = False
            x *= -1
        while x > 0:
            ans = ans * 10 + x % 10
            x /= 10

        if positive:
            return ans if ans <= 2147483647 else 0
        else:
            return -ans if ans <= 2147483648 else 0


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    print " ---> Success"
