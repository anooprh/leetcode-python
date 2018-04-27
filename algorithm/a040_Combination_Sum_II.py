import os


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = set()
        line = []
        self.helper(candidates, target, res, line)
        return list(map(lambda x: list(x), res))

    def helper(self, candidates, target, res, line):
        if target == 0:
            res.add(tuple(line))
            return

        for i, n in enumerate(candidates):
            if n <= target:
                line.append(n)
                self.helper(candidates[i + 1:], target - n, res, line)
                line.pop()


def checkSameList(l1, l2):
    return set(map(lambda x : tuple(x), l1)) == set(map(lambda x : tuple(x), l2))

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert checkSameList(Solution().combinationSum2([1, 5, 2, 3, 1, 5, 1, 2, 4, 1, 4], 3), [[1, 1, 1], [1, 2], [3]])
    print(" ---> Success")
