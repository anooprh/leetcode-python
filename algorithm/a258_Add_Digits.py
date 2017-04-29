import os


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else num % 9 if num % 9 != 0 else 9


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    def f(x):
        return x if x < 10 else f(sum([int(c) for c in str(x)]))
    d = {n: f(n) for n in range(1000)}
    for i in range(1000):
        assert Solution().addDigits(i) == d[i]
    print(" ---> Success")
