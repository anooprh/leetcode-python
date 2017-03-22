import os


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i - 1])
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().maxProfit([12, 9, 15, 9, 12]) == 9
    print " ---> Success"
