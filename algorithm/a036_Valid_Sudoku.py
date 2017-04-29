import os


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rCh = [[False for _ in range(10)] for _ in range(10)]
        cCh = [[False for _ in range(10)] for _ in range(10)]
        dCh = [[False for _ in range(10)] for _ in range(10)]
        for rowNum, rc in enumerate(board):
            for colNum, c in enumerate(rc):
                if c == ".": continue
                if rCh[rowNum][int(c) - 1]:
                    return False
                else:
                    rCh[rowNum][int(c) - 1] = True
                if cCh[colNum][int(c) - 1]:
                    return False
                else:
                    cCh[colNum][int(c) - 1] = True

                if dCh[((rowNum // 3) * 3) + colNum // 3][int(c) - 1]:
                    return False
                else:
                    dCh[((rowNum // 3) * 3) + colNum // 3][int(c) - 1] = True
        return True


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]) == True
    assert Solution().isValidSudoku(
        [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
         "9........"]) == True
    print(" ---> Success")
