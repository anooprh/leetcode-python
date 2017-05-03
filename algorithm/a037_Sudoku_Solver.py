import os


class Solution(object):
    def solve_internal(self, board, rv, cv, qv, start=(0, 0)):
        if start == (9, 0):
            return True
        used = False
        for i in range(start[0], 9):
            for j in range(start[1] if not used else 0, 9):
                used = True
                if board[i][j] != '.': continue
                quadrant = i // 3 * 3 + j // 3
                possible = rv[i].intersection(cv[j]).intersection(qv[quadrant])
                for w in possible:
                    board[i][j] = w
                    rv[i].remove(w)
                    cv[j].remove(w)
                    qv[quadrant].remove(w)
                    rn = i if j != 8 else i + 1
                    cn = j + 1 if j != 8 else 0
                    if self.solve_internal(board, rv, cv, qv, (rn, cn)):
                        return True
                    else:
                        board[i][j] = '.'
                        rv[i].add(w)
                        cv[j].add(w)
                        qv[quadrant].add(w)
                return False
        return True
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rv = [{'1', '2', '3', '4', '5', '6', '7', '8', '9'} for _ in range(9)]
        cv = [{'1', '2', '3', '4', '5', '6', '7', '8', '9'} for _ in range(9)]
        qv = [{'1', '2', '3', '4', '5', '6', '7', '8', '9'} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.': continue
                rv[i].remove(c)
                cv[j].remove(c)
                qv[i // 3 * 3 + j // 3].remove(c)

        self.solve_internal(board, rv, cv, qv)


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    input_pp = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5",
                "....8..79"]
    exp_pp = ["534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635",
              "345286179"]

    str_to_list = lambda row: list(row)
    inp = list(map(str_to_list, input_pp))
    exp = list(map(str_to_list, exp_pp))
    Solution().solveSudoku(inp)
    assert inp == exp
    print(" ---> Success")
