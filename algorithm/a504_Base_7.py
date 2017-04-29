import os


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        n = abs(num)
        res = ''
        while n > 0:
            res = str(n % 7) + res
            n //= 7
        return '-' + res if num < 0 else res


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().convertToBase7(100) == '202'
    assert Solution().convertToBase7(-7) == '-10'
    print(" ---> Success")
