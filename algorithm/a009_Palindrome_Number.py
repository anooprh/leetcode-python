import os


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        r = 10
        while x // r > 0: r *= 10
        r //= 10

        while x > 0:
            if x % 10 != x // r:
                return False
            x %= r
            x //= 10
            r //= 100
        return True


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isPalindrome(123) == False
    assert Solution().isPalindrome(1221) == True
    print(" ---> Success")
