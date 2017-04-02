import os


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        titleCap = self.isCapital(word[0])
        otherCap = None
        for c in word[1:]:
            if otherCap is not None:
                if self.isCapital(c) is not otherCap:
                    return False
            else:
                otherCap = self.isCapital(c)

        if otherCap is not None:
            return not (otherCap and not titleCap)
        return True

    def isCapital(self, c):
        return ord(c) >= ord("A") and ord(c) <= ord("Z")


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().detectCapitalUse("abcd") == True
    assert Solution().detectCapitalUse("ABCD") == True
    assert Solution().detectCapitalUse("Abcd") == True
    assert Solution().detectCapitalUse("AbBd") == False
    print " ---> Success"
