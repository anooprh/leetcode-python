import collections
import os

# Incomplete

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """



if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    length = Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print length
    assert length == 5
    print " ---> Success"
