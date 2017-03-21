import os


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        table = {}
        g = self.compute_graph(wordList)
        ans = float('inf')

        if beginWord in wordList:
            ans = 1 + self.bfs(g, beginWord, endWord, set(), table)
        else:
            for word in wordList:
                if self.isOneDiff(beginWord, word):
                    ans = min(ans, 2 + self.bfs(g, word, endWord, set(), table))
        if ans > len(wordList):
            ans = 0
        return ans

    def compute_graph(self, wordList):
        g = {}
        for word in wordList:
            g[word] = []
            for c_word in wordList:
                if self.isOneDiff(word, c_word):
                    g[word].append(c_word)
        return g

    def isOneDiff(self, word1, word2):
        ans = False
        if len(word1) is not len(word2):
            return False
        for c1, c2 in zip(word1, word2):
            if c1 is not c2 and ans is False:
                ans = True
            elif c1 is not c2 and ans is True:
                ans = False
                break
        return ans

    def bfs(self, graph, start, end, visited, table):
        if start in table:
            return table[start]

        if start == end:
            return 0

        ans = float('inf')
        visited.add(start)
        for child in graph[start]:
            if child not in visited:
                ans = min(ans, 1 + self.bfs(graph, child, end, visited, table))
        visited.remove(start)
        table[start] = ans

        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    print " ---> Success"
