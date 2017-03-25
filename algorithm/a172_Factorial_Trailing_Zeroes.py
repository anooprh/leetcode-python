import os


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        v, ans = 5, 0

        while n / v > 0:
            ans += n / v
            v *= 5
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().trailingZeroes(1) == 0
    assert Solution().trailingZeroes(5) == 1
    assert Solution().trailingZeroes(10) == 2
    assert Solution().trailingZeroes(11) == 2
    assert Solution().trailingZeroes(17) == 3
    assert Solution().trailingZeroes(20) == 4
    assert Solution().trailingZeroes(25) == 6
    assert Solution().trailingZeroes(25) == 6
    print " ---> Success"
