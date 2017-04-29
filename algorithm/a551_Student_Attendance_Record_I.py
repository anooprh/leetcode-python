import os


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aseen = False
        for i in range(len(s)):
            if s[i] == 'A':
                if aseen:
                    return False
                else: aseen = True
            elif s[i] == 'L' and (i >1 and s[i - 1] == 'L' and s[i-2] == 'L'):
                return False

        return True


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().checkRecord('PPALLP') == True
    assert Solution().checkRecord('PPALLL') == False
    print(" ---> Success")
