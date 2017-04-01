import os


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        kbd = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        k = {}
        for rowNum, row in enumerate(kbd):
            for char in row:
                k[char] = rowNum
                k[char.lower()] = rowNum

        return [word for word in words if self.sameRow(word, k)]

    def sameRow(self, word, k):
        for i in range(len(word)):
            if i != 0 and k[word[i]] != k[word[i - 1]]:
                return False
        return True


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
assert Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
print " ---> Success"
