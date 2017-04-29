import os


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(['1' if c == '0' else '0' for c in bin(num)[2:]]), 2)


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().findComplement(5) == 2
    assert Solution().findComplement(1) == 0
    print(" ---> Success")
