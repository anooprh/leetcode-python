import os
import bisect


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        ans, rem, div, Q = 0, dividend, divisor, 1

        while rem >= divisor:
            rem -= div
            ans += Q
            Q += Q
            div += div
            if rem < div:
                Q = 1
                div = divisor

        return max(-ans, -2147483648) if negative else min(ans, 2147483647)


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().divide(12, 6) == 2
    assert Solution().divide(12, 9) == 1
    assert Solution().divide(12, -9) == -1
    assert Solution().divide(-12, 9) == -1
    assert Solution().divide(-1, -1) == 1
    assert Solution().divide(10, 3) == 3
    print " ---> Success"
