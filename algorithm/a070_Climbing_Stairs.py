import os


class Solution(object):
    def climbStairs(self, n, table={}):
        """
        :type n: int
        :rtype: int
        """
        if n in table: return table[n]
        if n == 0:
            ans = 0
        elif n == 1:
            ans = 1
        elif n == 2:
            ans = 2
        else:
            ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        table[n] = ans
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    print " ---> Success"
