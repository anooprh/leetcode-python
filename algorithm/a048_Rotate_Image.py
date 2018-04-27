import os


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n // 2)):
            for j in range(i, n - i - 1):
                (x1, y1) = (i, j)
                (x2, y2) = (j, n - i - 1)
                (x3, y3) = (n - i - 1, n - j - 1)
                (x4, y4) = (n - j - 1, i)

                matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4] = \
                    matrix[x4][y4], matrix[x1][y1], matrix[x2][y2], matrix[x3][y3]

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    Solution().rotate(matrix)
    assert matrix == [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]
    print(" ---> Success")
