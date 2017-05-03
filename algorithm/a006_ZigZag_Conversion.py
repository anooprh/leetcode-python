import os


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        table = ['' for _ in range(numRows)]
        while i < len(s):
            j = 0
            while j < numRows and i < len(s):
                table[j] += s[i]
                j += 1
                i += 1
            j -= 2
            while j > 0 and i < len(s):
                table[j] += s[i]
                j -= 1
                i += 1

        return ''.join(table)


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().convert('PAYPALISHIRING', 3) == "PAHNAPLSIIGYIR"
    print(" ---> Success")
