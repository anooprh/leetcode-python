import os


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        return self.__change_internal(amount, 0, coins, [[-1] * (amount + 1) for _ in range(len(coins))])

    def __change_internal(self, bal, st, coins, table):
        if bal == 0:
            return 1
        if bal < 0 or st >= len(coins):
            return 0
        if table[st][bal] != -1:
            return table[st][bal]

        ans = self.__change_internal(bal - coins[st], st, coins, table)
        ans += self.__change_internal(bal, st + 1, coins, table)
        table[st][bal] = ans
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().change(5, [1, 2, 5]) == 4
    assert Solution().change(3, [2]) == 0
    assert Solution().change(10, [10]) == 1
    print(" ---> Success")
