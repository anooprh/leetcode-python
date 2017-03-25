import os


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        next = {
            "I": {"V", "X"},
            "X": {"L", "C"},
            "C": {"D", "M"},
        }
        ans = 0
        for i in range(len(s)):
            if i != len(s) - 1 and s[i] in next and s[i + 1] in next[s[i]]:
                ans -= table[s[i]]
            else:
                ans += table[s[i]]
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().romanToInt("I") == 1
    assert Solution().romanToInt("II") == 2
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("V") == 5
    assert Solution().romanToInt("VIII") == 8
    assert Solution().romanToInt("IX") == 9
    print " ---> Success"
