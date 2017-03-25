import os


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table = {
            1000: ["", "M", "MM", "MMM"],
            100: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            10: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            1: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        }
        v, ans = 1000, ""
        while v > 0:
            ans += table[v][num / v]
            num %= v
            v /= 10
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().intToRoman(1) == "I"
    assert Solution().intToRoman(2) == "II"
    assert Solution().intToRoman(4) == "IV"
    assert Solution().intToRoman(5) == "V"
    assert Solution().intToRoman(8) == "VIII"
    assert Solution().intToRoman(9) == "IX"
    print " ---> Success"
