import os


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_arr = [9999999999]
        for p in prices:
            min_arr.append(min(min_arr[-1], p))
        ans = 0
        for i, p in enumerate(prices):
            ans = max(ans, p - min_arr[i])
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    print(" ---> Success")
