import copy


class Solution(object):
    def isOkay(self, grid, row, col):
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 'Q':
                    if i == row:
                        return False
                    if j == col:
                        return False
                    if abs(row - i) == abs(col - j):
                        return False
        return True

    def isSolvable(self, grid, st, n):
        if st == n:
            return [grid]
        ans = []
        for j in range(n):
            if self.isOkay(grid, st, j):
                grid[st][j] = 'Q'
                v = self.isSolvable(grid, st + 1, n)
                for v1 in v:
                    ans.append(copy.deepcopy(v1))
                grid[st][j] = '.'
        return ans

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        grid = [['.' for _ in range(n)] for _ in range(n)]

        ans = []
        for i in range(n):
            grid[0][i] = 'Q'
            v = self.isSolvable(grid, 1, n)
            if len(v) > 0:
                for v1 in v:
                    ans.append([''.join(x) for x in v1])
                grid = [['.' for _ in range(n)] for _ in range(n)]
            else:
                grid[0][i] = '.'
        return ans


if __name__ == "__main__":
   s = Solution()
   assert s.solveNQueens(4) == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]