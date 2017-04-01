import os


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for rowNum, row in enumerate(grid):
            for colNum, val in enumerate(row):
                if val != 1: continue
                if rowNum == 0 or grid[rowNum - 1][colNum] == 0: ans += 1
                if rowNum == len(grid) - 1 or grid[rowNum + 1][colNum] == 0: ans += 1
                if colNum == 0 or grid[rowNum][colNum - 1] == 0: ans += 1
                if colNum == len(row) - 1 or grid[rowNum][colNum + 1] == 0: ans += 1
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().islandPerimeter([[0, 1, 0, 0],
                                       [1, 1, 1, 0],
                                       [0, 1, 0, 0],
                                       [1, 1, 0, 0]]) == 16
    print " ---> Success"
